# Independent mathematical audit

## correctness

PASS

The tetrahedral symmetry together with antipodal projection invariance reduces to x>=y>=z>=0. The four face-normal signs select edges whose two incident faces face opposite ways, giving the three difference terms if x<y+z and the four x±y,x±z terms if x>y+z. The formulas extend continuously to the boundary. In the triangular branch x-z<=1/sqrt(2); applying the chord bound for the concave sqrt(2-t^2) to all three differences gives P>=2(sqrt(2)+sqrt(6)) with equality requiring x=y=1/sqrt(2), z=0. In the other branch, with r^2=y^2+z^2, the even binomial series makes f(x+sqrt(s))+f(x-sqrt(s)) strictly concave in s. At fixed r its sum is minimized at s=0,r^2, giving the lower bound 4(sqrt(1-r^2)+sqrt(1+r^2)), strictly decreasing up to r=1/sqrt(2); equality gives the same normals. There are twelve oriented points or six unoriented axes. In the local normalized chart the branch line is exactly |q|=sqrt(2)|p|. The collapsing edge supplies 2 sqrt(2) sqrt(p^2+q^2) in the quadrilateral expansion with a smooth linear correction -2 sqrt(2/3)|p|; in the triangular branch the smooth terms give 4|q|/sqrt(3). The first-order gauge is continuous and positive off the origin; the O(s^2) remainder is uniform on each closed sector. Compactness localizes the small tail, and the surface Jacobian tends to one under scaling. Hence the rescaled conditional area is uniform on the gauge body (given the minimizing neighborhood), its triangle mark is the stated sector, and the twelve chart weights are equal. Polar integration in one quadrant and the Haar factor 12*4/(4*pi) give the exact coefficients. As a cross-check, the half-angle substitution gives A_4=A_3+3*pi*sqrt(3/2)/64 and the triangular fraction simplifies to 2/(4+pi*sqrt(3)). The printed decimals are quadrature approximations, not exact trailing digits; the exact formulas yield about 1.1953469179961410 and 0.21183303366328966. The uploaded checker was read, not executed. The independent /workspace/branches/review-replay.py checks local projected hulls and evaluates the transformed integral; the limit is proved analytically.

## originality

PASS

The regular tetrahedral projection model, three-versus-four silhouette partition, and moment quantities have prior coverage. On inspected evidence the distinct claim is the sharp near-minimum perimeter probability with its exact coefficient and perimeter-conditioned angular and silhouette law. Closely related area and chord tail theorems have different local gauges or events; this is not a change of units in those results. The competing stereology article remains an access risk, not negative evidence.

## value

PASS

The sharp rarity of a nearly shortest orthogonal shadow of a basic convex body is a natural invariant. The marked tangent body explains not just the exponent but the geometrically surprising roughly 21 percent triangular share, as opposed to one half under area conditioning, and gives limiting directions at the correct scale. This is a distinct geometric law, not an isolated integral without a motivated observable. It is specific to the stated tetrahedron and normalization; it does not give a full perimeter density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
