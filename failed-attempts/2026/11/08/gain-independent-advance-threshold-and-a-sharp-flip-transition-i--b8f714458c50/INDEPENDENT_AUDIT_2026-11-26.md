# Independent mathematical audit

## correctness

PASS

Writing h=g/a and Q(u)=u+h(1-F)tanh(u), the implicit sample equation is Q(u)=Fx. Q is a strictly increasing bijection, including at theta=0 and theta=1. The sample-coordinate map is Q(u_next)=Eu-h(F-E)tanh(u). The mesh derivative at x corresponding to u is m(q)=[E-h(F-E)q]/[1+h(1-F)q] with q=sech^2(u). It ranges from m(1) to E, with 1+m(1)=(1+E-h*Delta)/(1+h(1-F)); this proves the sharp exponential regimes. Interpolation has a bounded multiplier on each unit interval. At equality |P(x)|<|x| for x nonzero although the uniform derivative bound is one. Expanding Q and its inverse yields P(x)=-x+Kx^3+O(x^5), and differences of |x_k|^{-2} tend to 2K on non-finite-hitting orbits. Above threshold m(1)<-1; the equation P(c)=-c forces u=Cc and has exactly one positive solution since tanh(z)/z strictly decreases. Its derivative satisfies m(sech^2(Cc))>m(h_c/h)=-1, and is less than E; the cycle multiplier is the square of this derivative. Odd interpolation gives anti-periodicity. P(x)<x for x>0, so no nonzero fixed point, and the amplitude expansion follows from tanh(z)/z=1-z^2/3+O(z^4). An independent sample-coordinate numerical check at E=1/2, F=7/8, h_c=6 gave K=1/14 and k*x_k^2/7=0.999364 at k=100000; at h=6.3 it gave c=0.778482 and a two-step multiplier about 0.83864. These are corroboration, not the proof; the frozen script was not run.

## originality

FAIL

A distinct earlier Resultary result states the same phase and gain threshold, critical asymptotic and attracting antisymmetric tanh branch under the same sampling convention and a more general mesh length. The main finding is covered exactly, not merely suggested by network-level sufficient conditions. Including theta=1 and spelling out a Taylor error or no nonzero fixed point adds only immediate deductions.

## value

FAIL

The transition is mathematically meaningful, but this version reproduces the earlier useful classification. Restricting mesh length to one and adding the implicit right-endpoint step, a Taylor remainder, or the elementary fixed-point exclusion does not provide a separate scientific result of value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
