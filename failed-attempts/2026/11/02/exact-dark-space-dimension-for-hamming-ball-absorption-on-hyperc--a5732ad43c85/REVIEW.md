# Independent mathematical audit

## correctness

PASS

For Gamma positive on exactly the ball, the norm loss derivative is -2 times its expectation. Zero norm loss forces evolution in its kernel, so the dark subspace is the sum of free-adjacency energy eigenspaces restricted to the kernel of Gamma. This subspace reduces both adjacency and Gamma; a real eigenvalue on the complement would force a vector in the dark space. Thus the bright dynamics decay also in the presence of Jordan blocks, and the maximally mixed absorption is B/2^d, independent of the rates. For the rank computation, expansion of each Walsh character on the ball into inclusion rows is invertible by triangularity. On the Boolean layers the up operator U and its adjoint L satisfy [L,U]=(d-2j)I on layer j; for h in the kernel of L at level i, L U^a h=a(d-2i-a+1)U^(a-1)h. Consequently each harmonic chain extends through level d-i, and these orthogonal chains fill each layer by dimension telescoping. Inclusion rows from level j span the images of that layer under U^(w-j), up to a factorial, hence the stack up to r sees exactly chain starts i<=min(r,w,d-w). Their dimensions telescope to the asserted binomial bound with equality. The sector sum gives the bright formula, and the middle sector is dark in part at every smaller radius than floor(d/2). At d=2t the last prethreshold deficit is binom(2t,t)-binom(2t,t-1); at d=2t+1 it is twice binom(2t+1,t)-binom(2t+1,t-1). These are C_t and 2 C_(t+1), respectively. The central term (d-2r+1)binom(d,r) controls the fixed-r asymptotic. A separately written adjacency Krylov calculation modulo 101 gave dark dimensions 5,0,28,0,98,14,0 for (6,2),(6,3),(7,2),(7,3),(8,2),(8,3),(8,4), respectively; this is finite corroboration only.

## originality

FAIL

An indexed result under the same dynamical hypotheses gives the harmonic restriction maps for individual spheres. Those maps diagonalize in a common domain decomposition, not just separate scalar ranks. Stacking the first r+1 maps covers precisely the expected initial harmonic degrees, with guaranteed visibility of degree i at the sphere of radius i. This supplies the claimed ball rank and all its numerical consequences, even though the ball formula is not separately displayed. There is no inference about temporal priority from the two records' displayed dates.

## value

FAIL

The absorption threshold and residual dimensions are natural questions, but every claimed quantitative answer is obtained directly by stacking harmonics from the indexed sphere theorem and then carrying out elementary summation. The alternate inclusion-matrix calculation is correct but does not establish a separate scientifically valuable surviving claim in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
