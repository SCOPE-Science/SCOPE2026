"""Standalone standard-library regression checks for cyclic-skew-line geometry.

The exact infinite statements follow from the trigonometric proof in RESULT.md;
finite sampling here checks formulas and catches normalization mistakes.
"""
import math

def dist2(a,k,n,j,x,y,z):
    phi=2*math.pi*j/n
    u=(math.cos(phi),math.sin(phi))
    v=(-u[1],u[0])
    dx=x-a*u[0]; dy=y-a*u[1]
    return dx*dx+dy*dy+z*z-((dx*v[0]+dy*v[1])+k*z)**2/(1+k*k)

def main():
    count=0
    for a in (0.2,1.0,3.0):
      for k in (0.1,0.4,1.0,2.0):
        B=1+k*k; C=8*B*(2*B-1)+B/(k*k)
        for h in range(3):
          for t in (-0.44,-0.27,-0.09,0,0.09,0.27,0.44):
            theta=2*math.pi*h/3+t
            radial=4*a*B/math.cos(3*t)
            x=radial*math.cos(theta); y=radial*math.sin(theta)
            z=a*B/k*math.tan(3*t)
            distances=[dist2(a,k,3,j,x,y,z) for j in range(3)]
            expect=a*a*((4*B-1)**2+C*math.tan(3*t)**2)
            for value in distances:
              assert abs(value-expect) <= 1e-8*max(1,abs(expect)),(a,k,t,value,expect)
              count+=1
        for z in (-10.,-0.2,0,0.9,5.):
          for n in (3,4,5,7,12):
            ds=[dist2(a,k,n,j,0.,0.,z) for j in range(n)]
            assert max(abs(d-(a*a+z*z/B)) for d in ds)<1e-9*max(1,ds[0])
            count+=n
        for R in (1.2,2.0,8.0):
          z=math.sqrt(B*(R*R-1))*a
          ds=[dist2(a,k,3,j,0,0,z) for j in range(3)]
          assert max(abs(d-(a*R)**2) for d in ds)<1e-9*max(1,(a*R)**2)
          count+=3
    # The n>=4 statement follows from discrete Fourier orthogonality; samples test consistency.
    for n in (4,5,6,7,8,11):
      for k in (.2,.8,3):
        for x,y,z in ((1.,0.,0.),(.4,.3,.2),(3.,-1.,2.),(-.7,.9,-.1)):
          d=[dist2(1,k,n,j,x,y,z) for j in range(n)]
          assert max(d)-min(d)>1e-6
          count+=1
    print(f"PASS: {count} deterministic numerical consistency checks")

if __name__=='__main__':main()
