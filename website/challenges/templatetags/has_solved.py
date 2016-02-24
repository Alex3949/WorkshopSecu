from django import template

register = template.Library()

@register.filter
def has_solved(user, challenge):
    return user in challenge.resolved_by.all()
