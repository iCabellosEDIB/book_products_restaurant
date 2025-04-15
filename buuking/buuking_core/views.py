from django.views.generic import TemplateView
from .models import Member, Product, Buuking


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['members'] = Member.objects.all()
        context['product'] = Product.objects.all()
        context['buuking'] = Buuking.objects.all()
        context['table_buuking'] = Buuking.objects.all()

        return context
