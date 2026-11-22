# Independent mathematical audit

## correctness

PASS

On each cell, (D^2+1)e=mu with zero boundary values and Green G_h(s,t)=-sin(min(s,t))*sin(h-max(s,t))/sin h. The kernel sup is tan(h/2)/2 and exact integrated norm is cos(t-h/2)/cos(h/2)-1, maximized at cell midpoint. Antipodal symmetry forces cell mass <=M/2, explaining the sup factor 1/4; L1 sums both antipodal cells with full 2pi measure. For q(x)=|<v,x>| the profile |sin(theta-alpha)| has mu=2delta_alpha+2delta_(alpha+pi), M=4 and maximizes both. Since sum of N gaps is pi, h*>=pi/N with equality only equally spaced. Checked exact trigonometric identities for h=0.3,0.7,1.4,2.1; boundary masses contribute zero to Green cell errors. General all-fan result follows from Green representation, not finite script.

## originality

PASS

Unser Proposition 5.2 gives the same local Dirichlet kernel and rate on a uniform grid, including a nonsharp integrated upper bound, but not the jointly sharp exact unnormalized L1 constant, global antipodal factor, rank-one extremizer for every nonuniform fan, or minimax optimal design. Classical L-spline theory may have the local kernel norm; this is a real residual priority risk.

## value

PASS

Best constants for curvature-measure interpolation and exact optimal ray placement matter for numerical conic-spline approximation. Simultaneous seminorm equality and exact nonuniform minimax rule improve a merely rate-level error estimate; this natural optimal recovery problem supports mathematical value independently of code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
