from django import template

register = template.Library()   #register is an object.

#creating custom_filters using function

@register.filter(name='cut')        #decorator usage
def cut(value,arg):
		   """This cuts out all values of "arg" from the string"""
		   return value.replace(arg,'')

#register.filter('cut',cut)   #disable if decorator usage if not enable this
