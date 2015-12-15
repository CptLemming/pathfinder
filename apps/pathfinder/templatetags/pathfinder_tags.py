from django import template

register = template.Library()


@register.inclusion_tag('partials/node.html', takes_context=True)
def render_node(context, x, y):
    start = context['start']
    goal = context['goal']
    graph = context['graph']
    cost_so_far = context['cost_so_far']
    trees = context['trees']
    node = (x, y)
    return {
        'is_start_node': node == start,
        'is_goal_node': node == goal,
        'is_wall_node': node in graph.walls,
        'is_tree_node': node in trees,
        'node_cost': cost_so_far.get(node, 0),
        'x': x,
        'y': y,
    }


@register.filter
def get_range(value):
    return range(value)
