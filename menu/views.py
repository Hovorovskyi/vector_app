from django.shortcuts import render
from django.views.generic import ListView
from .models import MenuItem


class MenuItemView(ListView):
    model = MenuItem
    template_name = 'menu/menu_list.html'
    context_object_name = 'menu_items'

    def get(self, request, *args, **kwargs):
        category = request.GET.get('category')
        menu_items = MenuItem.objects.all()
        if category:
            menu_items = menu_items.filter(category=category)
        return render(request, self.template_name, {'menu_items': menu_items})

        # def get_queryset(self):
        #     queryset = super().get_queryset()
        #     category = self.request.GET.get('category')
        #     if category:
        #         queryset = queryset.filter(category=category)
        #     return queryset

    # def menu_view(request, category=None):
    #     if category:
    #         menu_item = MenuItem.objects.filter(category=category)
    #         return render(request, 'menu/menu_list.html', {'menu_items': menu_item})
    #     else:
    #         menu_item = MenuItem.objects.all()
    #         return render(request, 'menu/menu_list.html', {'menu_items': menu_item})
