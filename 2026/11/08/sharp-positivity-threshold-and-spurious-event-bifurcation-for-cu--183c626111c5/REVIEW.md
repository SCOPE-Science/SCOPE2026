# Independent mathematical audit

## correctness

PASS

PASS: for y0>0, lambda,h>0 and z=lambda h, cubic Hermite with exact endpoint value and derivatives has H_z(s)=1-zs+B(z)s²+A(z)s³. Differentiating including exp(-z) gives ∂_z H_z(s)=-s(1-s)²-e^-z s²[2-s+z(1-s)]<0 in interior. Its compact minimum strictly decreases continuously from 1 at z=0 to -infinity for z→infinity, yielding unique positivity threshold. Endpoint values positive force a unique interior even-multiplicity root at first contact; a cubic forces double root, and for z beyond it exactly two simple interior zeros. Nonzero ∂_z and positive curvature give square-root opening K=sqrt(-2 H_z/H_ss). Independent symbolic identity and numerical saddle reproduced z*=3.86930633627, s*=0.675694826 and K~0.336550838. Finite rational Bernstein certificates in verify.py were inspected but not mistaken for proof or fully replayed here.

## originality

PASS

PASS best-of-knowledge: classical cubic Hermite nonnegativity/monotonicity studies (Dougherty–Edelman–Hyman 1989, Higham 1992) provide general sufficient shape constraints, not the fully sharp exponential exact-endpoint step-length boundary, globally exactly-two false events and local sqrt opening in this model. ENO positive interpolators modify slopes/data and are not this unmodified cubic. Relevant full primary sections were inspected where accessible; older exact exponential special cases may exist outside bounded search.

## value

PASS

PASS: false zero-events in interpolated positive ODE trajectories motivate the exact natural dimensionless sharp interpolation-step threshold. Global classification and sqrt-bifurcation constant provide useful numerical-analysis event detection boundary despite being a scalar exponential specialization. This is a motivated concrete invariant, not just an arbitrary numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
