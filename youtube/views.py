from django.shortcuts import render, redirect
from .models import VideoList, Video, VideoComment, VideoSubComment
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.db.models import Q

def index(request):
    params = {
    		'vlist': VideoList.objects.order_by('title'),
    		'title':"Video List - Youtube",
    	}

    return render(request, 'youtube/index.html', params)

def videos(request, title):

	vidlist = VideoList.objects.get(title=title)
	vid = Video.objects.filter(video_list=vidlist).first()
	if vid:
		return redirect(f'/youtube/videos/{title}/{vid.id}/{vid.title}')
	raise Http404("This List is Empty")

def video(request, title, id, video):
	allvid = Video.objects.filter(video_list=VideoList.objects.get(title=title))
	vid = allvid.get(id=id, title=video)
	nextvid = allvid.filter(id__gt = vid.id).first()
	previd = allvid.filter(id__lt = vid.id).last()

	if request.method == 'POST':
		comm = request.POST.get('comm')
		comm_id = request.POST.get('comm_id') #None

		if comm_id:
			VideoSubComment(video=vid,
					user = request.user,
					comm = comm,
					comment = VideoComment.objects.get(id=int(comm_id))
				).save()
		else:
			VideoComment(video=vid, user=request.user, comm=comm).save()
		
		return redirect(f'/youtube/videos/{title}/{vid.id}/{vid.title}')

	comments = []
	for c in VideoComment.objects.filter(video=vid):
		comments.append([c, VideoSubComment.objects.filter(comment=c)])

	params = {
		'allvid': allvid,
		'vid': vid,
		'nextvid': nextvid,
		'previd': previd,
		'title': vid.title,
		'comments': comments,
    	'title':f"{vid.title} - Youtube",
	}
	return render(request, 'youtube/video.html', params)


def search(request, query):
	vidlist = VideoList.objects.filter(
		Q(title__icontains = query) |
		Q(description__icontains = query)
		).distinct()

	vid = Video.objects.filter(
		Q(title__icontains = query) |
		Q(desc__icontains = query) | 
		Q(tags__icontains = query)
		).distinct()
	parms = {
		'vidlist': vidlist,
		'vid': vid,
    	'title':f"search result : {query}",
		
		}
	return render(request, 'youtube/search.html', parms)