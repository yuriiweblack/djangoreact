from django.db import models

class BlogCategory(models.Model):

    name = models.CharField(max_length=255, verbose_name="name category")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class BlogPostQuerySet(models.QuerySet):

    def find_by_title_in_qs(self, post_title):
        return self.filter(title__icontains=post_title)




class BlogPostManager(models.Manager):

    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().filter(in_archive=False)

    def find_by_title_in_qs(self, post_title):
        return self.get_queryset().find_by_title_in_qs(post_title)


class BlogPost(models.Model):

    blog_categoty = models.ForeignKey(BlogCategory, verbose_name="name category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="name post")
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_posts/", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    in_archive = models.BooleanField(default=False)
    objects = BlogPostManager()

    def __str__(self):
        return f"{self.title} from catecory \"{self.blog_categoty.name}\""

