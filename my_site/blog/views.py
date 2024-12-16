from datetime import date

from django.shortcuts import render

# Create your views here.
all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.png",
        "author": "Dipankar",
        "date": date(2024, 12, 15),
        "title": "Mountain Hiking",
        "excerpt": """ There is nothing like hiking in the mountains. The fresh air, the beautiful scenery, the
                    sense of accomplishment when you reach the summit. It is an experience like no other. """,

        "content": '''
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
                  
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
                  
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
                  
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
                  
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
                  
                  
                    ''',

    },
    {
        "slug": "programming-is-fun",
        "image": "coding.png",
        "author": "mitra",
        "date": date(2024, 12, 10),
        "title": "Programming Is Great!",
        "excerpt": '''Did you ever spend hours searching that one error in your code? Yep - that's what happened to me"
                   yesterday...''',
        "content": """
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.png",
        "author": "Maximilian",
        "date": date(2024, 11, 10),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                  aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                  velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_dates(post) -> date | None:
    # Helper function to extract the date from a post
    return post.get("date", None)


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_dates, reverse=True)
    latest_posts = sorted_posts[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
