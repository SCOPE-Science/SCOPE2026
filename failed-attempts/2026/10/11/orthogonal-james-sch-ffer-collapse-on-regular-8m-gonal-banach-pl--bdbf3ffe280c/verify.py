import math

def polygon(N):
    a=math.pi/N
    c=math.cos(a)
    s=math.sin(a)
    normals=[
        (math.cos(2*k*a)/c, math.sin(2*k*a)/c)
        for k in range(N)
    ]
    return a,c,s,normals

def norm(z,normals):
    return max(f[0]*z[0]+f[1]*z[1] for f in normals)

checks=0
for m in range(1,13):
    N=8*m
    a,c,s,F=polygon(N)

    # Smooth-edge branch x=(c,t), y=(0,c).
    for j in range(101):
        t=-s+2*s*j/100
        x=(c,t); y=(0.0,c)
        A=norm((x[0]+y[0],x[1]+y[1]),F)
        B=norm((x[0]-y[0],x[1]-y[1]),F)
        eA=math.sqrt(2)+t/(math.sqrt(2)*c)
        eB=math.sqrt(2)-t/(math.sqrt(2)*c)
        assert abs(A-eA)<2e-11
        assert abs(B-eB)<2e-11
        assert min(A,B)<=math.sqrt(2)+2e-11
        assert max(A,B)>=math.sqrt(2)-2e-11
        checks+=1

    # Vertex first-half Birkhoff sector.
    x=(c,s)
    for j in range(101):
        r=s*j/100
        y=(-r,c)
        A=norm((x[0]+y[0],x[1]+y[1]),F)
        B=norm((x[0]-y[0],x[1]-y[1]),F)
        eA=math.sqrt(2)+(s-r)/(math.sqrt(2)*c)
        eB=math.sqrt(2)-(s-r)/(math.sqrt(2)*c)
        assert abs(A-eA)<2e-11
        assert abs(B-eB)<2e-11
        assert min(A,B)<=math.sqrt(2)+2e-11
        assert max(A,B)>=math.sqrt(2)-2e-11
        checks+=1

    # Quarter-turn equality at vertex and edge midpoint.
    for x in [(c,s),(c,0.0)]:
        y=(-x[1],x[0])
        A=norm((x[0]+y[0],x[1]+y[1]),F)
        B=norm((x[0]-y[0],x[1]-y[1]),F)
        assert abs(A-math.sqrt(2))<2e-11
        assert abs(B-math.sqrt(2))<2e-11

print(
    "VERIFY_OK "
    f"regular_8m_polygons=12 branch_checks={checks} "
    "J_perp=g_perp=sqrt2"
)
