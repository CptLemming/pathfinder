from django.views.generic import TemplateView

from .grids import GridWithWeights
from .search import a_star_search


class PathfinderView(TemplateView):
    template_name = 'pathfinder.html'

    def get_context_data(self, **kwargs):
        walls = [
            (21, 0), (22, 0),
            (21, 1), (22, 1),
            (21, 2), (22, 2),
            (21, 3), (22, 3),
            (21, 4), (22, 4),
            (21, 5), (22, 5), (23, 5), (24, 5), (25, 5),
            (21, 6), (22, 6), (23, 6), (24, 6), (25, 6),
        ]
        trees = [
            (19, 1), (20, 1),
            (19, 2), (20, 2),
        ]
        tree_weight = int(self.request.GET.get('tree_weight', 2))
        weights = {position: tree_weight for position in trees}
        width = 30
        height = 15

        graph = GridWithWeights(width, height)
        graph.walls = walls
        graph.weights = weights
        start = (20, 0)
        goal = (23, 0)
        came_from, cost_so_far = a_star_search(graph, start, goal)

        return {
            'graph': graph,
            'came_from': came_from,
            'cost_so_far': cost_so_far,
            'start': start,
            'goal': goal,
            'trees': trees,
        }
