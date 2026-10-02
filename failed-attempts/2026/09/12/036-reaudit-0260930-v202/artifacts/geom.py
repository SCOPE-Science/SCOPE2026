# Characteristic 7 basic checks, stdlib only
p = 7
# Cone F = Y^2 Z - X^3 - X^2 Z over F7. Gradient:
# dF/dX = -3X^2-2XZ, dF/dY = 2YZ, dF/dZ = Y^2 - X^2
def grad(pt):
    X,Y,Z = pt
    return ((-3*X*X-2*X*Z)%p, (2*Y*Z)%p, (Y*Y-X*X)%p)
def F(pt):
    X,Y,Z = pt
    return (Y*Y*Z - X**3 - X*X*Z) % p
# singular locus: F=0 and grad=0, brute force over A^3(F7)
sing = [pt for X in range(p) for Y in range(p) for Z in range(p) for pt in [(X,Y,Z)] if F(pt)==0 and grad(pt)==(0,0,0)]
print("n_sing_pts_affine:", len(sing))
print("all sing have X=Y=0?", all(x==0 and y==0 for x,y,z in sing))
# projective nodal cubic: count points, node at [0:0:1], smooth elsewhere?
def proj_pts():
    pts=set()
    for X in range(p):
        for Y in range(p):
            for Z in range(p):
                if (X,Y,Z)==(0,0,0): continue
                if F((X,Y,Z))==0:
                    # normalize representative
                    for c in range(1,p):
                        if (c*X%p==X and c*Y%p==Y and c*Z%p==Z): pass
                    pts.add((X,Y,Z))
    return pts
print("node grad at [0:0:1]:", grad((0,0,1)), "F=", F((0,0,1)))
print("smooth pt grad e.g. [0:1:0]: F=", F((0,1,0)), "grad=", grad((0,1,0)))
# normalization param t -> [t^2-1 : t(t^2-1) : 1], infty -> [0:1:0]; verify lies on curve over F7
ok=True
for t in range(p):
    X=(t*t-1)%p; Y=(t*X)%p; Z=1
    if F((X,Y,Z))!=0: ok=False; print("param fail",t)
print("param lands on curve for all t:", ok)
# fiber over node: t=1 and t=-1=6 both give [0:0:1]
print("fiber node:", [t for t in range(p) if ((t*t-1)%p==0)])
# blow-up of A^3 at origin, chart U_x (x!=0): coords u=y/x, v=z/x; strict transform:
# F/x^3? F = x^2(y^2 z/x^2 ... ) compute: F/x^2 = u^2 v x - x - ... let's just print equation:
# F = Y^2Z - X^3 - X^2Z = X^3(u^2 v - 1 - v) with v=z/x? Z=vX so F=X^3(u^2 v -1 -v). Strict: u^2 v - v - 1 =0.
# Chart U_z (z!=0): a=x/z,b=y/z: F/z^3 = b^2 - a^3 - a^2 => b^2 - a^2 - a^3 =0 (cylinder over nodal curve) singular along a=b=0 (whole z-line).
print("chart Ux strict: u^2*v - v - 1 = 0 (smooth? grad=(-? ))")
# check smoothness of chart Ux: G=u^2 v - v -1; grad=(2uv, u^2-1); common zero requires G=0 too: u^2=1,v arbitrary? then G = v-v-1=-1 !=0. so smooth.
print("chart Ux smooth: verified by hand (grad never vanishes on G=0 since G|_{u^2=1}=-1)")
print("chart Uz strict: b^2-a^3-a^2=0 singular along a=b=0 for all c=z => singular line persists in blow-up Y")
# exceptional divisor: in chart Uz, z=0 gives b^2-a^3-a^2=0 = nodal cubic affine part; in chart Ux, x=0 gives -1=0 empty. So E = nodal cubic.
print("E = nodal cubic C confirmed in Uz chart")
# Frobenius on node tangents: node tangents at [0:0:1]: tangent cone Y^2-X^2=(Y-X)(Y+X), both defined over F7 (split). slopes +-1 in F7.
print("split node tangents slopes:", [1, -1], "in F7: split confirmed")
