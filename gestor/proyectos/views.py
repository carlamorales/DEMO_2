from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Proyecto, Tarea

class ProyectoListaView(ListView):
    model = Proyecto
    template_name = "proyectos/lista.html"
    context_object_name = "proyectos"
    queryset = Proyecto.objects.filter(activo=True).order_by("fecha_inicio")

class ProyectoDetalleView(DetailView):
    model = Proyecto
    template_name = "proyectos/detalle.html"
    context_object_name = "proyecto"

class TareaCrearView(CreateView):
    model = Tarea
    fields = ["titulo", "hecho"]
    template_name = "proyecto/tarea_form.html"

    def get_success_url(self):
        return reverse_lazy("proyecto_detalle", kwargs={"pk":self.kwargs["pk"]})
    
    def form_valid(self, form):
        form.instance.proyecto_id = self.kwargs["pk"]
        return super().form_valid(form)
