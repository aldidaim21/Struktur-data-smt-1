new = type('new', (object,),
           dict(var1='aldi daim', b=2009))


print(type(new))
print(type(new))


class test:
    a = "aldi daim"
    b = 2009


newer = type('newer', (test, ),
             dict(a="aldi", b=2018))

print(type(newer))
print(vars(newer))
