#!/usr/bin/env python3
"""Numerical corroboration of an exact concavity-and-contact argument."""
import math
h=1/math.sqrt(3)
def f(u):return math.sqrt(1-u*u)+math.sqrt(1-(u+0.5)**2)-math.sqrt(3)/2
def df(u):return -u/math.sqrt(1-u*u)-(u+0.5)/math.sqrt(1-(u+0.5)**2)
def root_expression(u):return f(u)+u*df(u)
l,r=0.0,0.499
assert root_expression(l)>0 and root_expression(r)<0
for _ in range(120):
 m=(l+r)/2
 if root_expression(m)>0:l=m
 else:r=m
u=(l+r)/2;v=f(u)/2;c=h+v-math.sqrt(1-u*u)
V=[(0,h),(-.5,-h/2),(.5,-h/2)]
points=[(sx*u,c+sy*v) for sx in (-1,1) for sy in (-1,1)]
res=[1-(x-a)**2-(y-b)**2 for x,y in points for a,b in V]
assert min(res)>-1e-12 and abs(root_expression(u))<1e-12
assert abs(4*u*v-0.4197167574230241)<2e-12
assert u>v and c<0
for k in range(1,501):
 t=(k/501)*.5
 assert 2*u*f(u)>=2*t*f(t)-1e-12
print('PASS: root, contacts, all 12 disk checks, 500 area comparisons')
print('u,v,c,area =',u,v,c,4*u*v)
