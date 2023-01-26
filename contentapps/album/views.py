from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import JsonResponse
from django.http import Http404
from .models import Album


class AlbumList(ListView):
    model = Album
    context_object_name = "albums"
    template_name = "album/album_list.html"
    paginate_by = 10
    queryset = Album.objects.exclude(visibility='h').order_by('-created_date')


class AlbumOverview(DetailView):
    model = Album
    context_object_name = "album"
    template_name = "album/album_overview.html"

    def dispatch(self, request, *args, **kwargs):
        result = super().dispatch(request, *args, **kwargs)
        pk = int(kwargs['pk'])
        album = Album.objects.get(pk=pk)
        visible = album.is_visible(request.user)
        if visible or request.user.has_perm('content.change_album'):
            return result
        else:
            return redirect('auth_login')


class AlbumImageView(TemplateView):

    template_name = "album/album_image.html"

    def dispatch(self, request, *args, **kwargs):
        result = super().dispatch(request, *args, **kwargs)
        pk = int(kwargs['pk'])
        album = Album.objects.get(pk=pk)
        if album.is_visible(request.user) or request.user.has_perm('content.change_album'):
            return result
        else:
            return redirect('auth_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num = int(kwargs['num'])
        pk = int(kwargs['pk'])
        try:
            album = Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404("Albumet finnes ikke.")
        context['album'] = album

        images = album.images.order_by('num').all()
        paginator = Paginator(images, 1)
        try:
            page_obj = paginator.page(num)
        except (EmptyPage, PageNotAnInteger):
            page_obj = paginator.page(1)

        context['page_obj'] = page_obj
        try:
            context['image'] = page_obj.object_list[0]
        except IndexError:
            # There are no images
            pass

        return context


@permission_required("album.create_album")
def multiple_file_upload(request):
    files = []

    for field, file in request.FILES:
        files.append({
            "name": file.name,
            "size": file.size,
            "url": file.url,
            "thumbnailUrl": file.url,
            "deleteUrl": file.url,
            "deleteType": "DELETE"
        })

    return JsonResponse({"files": files})
