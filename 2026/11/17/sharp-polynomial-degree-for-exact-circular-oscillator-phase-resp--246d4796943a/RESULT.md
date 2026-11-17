# Sharp polynomial degree for exact circular oscillator phase-response synthesis

## Finding

Let \(\omega>0\), and prescribe the physical-time unit-circle trajectory
\[p(t)=(\cos(\omega t),\sin(\omega t)).\]
Let \(h\) be a real trigonometric polynomial with highest nonzero Fourier order \(m\geq0\) (with \(m=0\) for constants, including zero). Consider real polynomial planar vector fields \(F\) for which this parametrized circle is an exponentially attracting periodic orbit and whose **normalized asymptotic-phase gradient** on it is
\[Z(\vartheta)=Jp(\vartheta)+h(\vartheta)p(\vartheta),\qquad J(x,y)=(-y,x),\qquad p(\vartheta)=(\cos\vartheta,\sin\vartheta).\]
The normalization is \(Z\cdot F(p)=\omega\), and \(\vartheta=\omega t\). Then the least possible total polynomial degree of \(F\) is **exactly** \(m+3\). This lower bound holds among **all** polynomial planar fields, without requiring rotational equivariance or uniform transverse damping. For every prescribed \(\kappa>0\), a degree-\(m+3\) realization exists with transverse Floquet exponent \(-\kappa\), whose unit circle attracts every nonzero initial state and is its only nonconstant periodic orbit. Every degree-minimal realization necessarily has a constant instantaneous linear radial damping rate along the unit circle.

In particular, the fifth-harmonic Cartesian phase-response example in [1] has radial phase sensitivity \(h(\vartheta)=2\sin(2\vartheta)-2\sin(4\vartheta)\), so its least possible polynomial degree is exactly **seven**. The degree-seven numerical design reported in [1] therefore meets the sharp algebraic lower bound; an explicit exact degree-seven alternative is constructed below.

## Assumptions and scope

A polynomial vector field is a pair \(F=(P,Q)\) with \(P,Q\in\mathbb R[x,y]\), and its degree is the larger total degree. The orbit is required to be *the precise parametrized* unit circle with uniform physical angular speed \(\omega\), not just a topologically circular orbit or an orbit after time reparametrization. The normalized phase gradient is the differential of the asymptotic phase function taking values in angular units, with \(\dot\Theta=\omega\). Exponential attraction gives a well-defined smooth phase gradient near the periodic orbit. The radial function \(h\) is completely arbitrary subject only to its finite Fourier support; no smallness, parity, or positivity assumption is made. The lower bound uses no constraint on behavior elsewhere in the plane.

## Proof

**1. Polynomial divisibility.** Put \(R=x^2+y^2\). Since \(F(p(\vartheta))=\omega Jp(\vartheta)\), both components of \(F-\omega J(x,y)\) vanish for every \(R=1\). Each is therefore divisible in \(\mathbb R[x,y]\) by \(R-1\): division as a polynomial in \(y\) by \(y^2+x^2-1\) leaves a remainder \(A(x)y+B(x)\). Evaluating at both values \(y=\pm\sqrt{1-x^2}\) for \(-1<x<1\) forces \(A=B=0\). Thus
\[F(x,y)=\omega J(x,y)+(R-1)G(x,y),\]
with \(G\) a polynomial pair. Unless \(G=0\), \(\deg F=\deg G+2\); the degree-\(\deg G+2\) term cannot cancel the linear rotation term. The case \(G=0\) is a linear center and has no exponentially attracting cycle.

**2. Phase-adjoint restriction.** On the unit circle define the real trigonometric polynomials
\[k(\vartheta)=p(\vartheta)\cdot G(p(\vartheta)),\qquad s(\vartheta)=Jp(\vartheta)\cdot G(p(\vartheta)).\]
In polar variables \((r,\vartheta)\), the normal and angular linearization at \(r=1\) is
\[\dot{(r-1)}=2k(\vartheta)(r-1)+O((r-1)^2),\quad\dot\vartheta=\omega+2s(\vartheta)(r-1)+O((r-1)^2).\]
By the prescribed phase gradient, locally \(\Theta(r,\vartheta)=\vartheta+h(\vartheta)(r-1)+O((r-1)^2)\). Differentiating \(\dot\Theta=\omega\) at \(r=1\) gives the necessary identity
\[\boxed{\ s=-\tfrac{\omega}{2}h'-kh.\ }\tag{1}\]
This is equivalent to the normalized adjoint equation along the orbit, and is exact.

**3. Sharp Fourier lower bound.** Identify a real pair \((a,b)\) with \(a+ib\). On \(R=1\), the polynomial pair \(G\) becomes the trigonometric polynomial
\[G_1(p(\vartheta))+iG_2(p(\vartheta))=e^{i\vartheta}[k(\vartheta)+is(\vartheta)].\tag{2}\]
If \(D=\deg G\), the left side has no Fourier frequency of absolute value exceeding \(D\). Suppose \(m\ge1\). If \(k\) has positive maximal Fourier frequency \(N\ge1\), the product \(kh\) has a nonzero Fourier coefficient at frequency \(m+N\), since the leading complex coefficients of real trigonometric polynomials multiply without cancellation. Neither \(k\) nor \(h'\) has this frequency. Equation (1) then makes the right side of (2) have a nonzero coefficient at frequency \(m+N+1\). Hence \(D\ge m+N+1\ge m+2\).

If \(k\) is constant (possibly zero), write \(h_m\ne0\) for the coefficient of \(e^{im\vartheta}\). The coefficient of \(e^{im\vartheta}\) in \(s\) is \(-(im\omega/2+k)h_m\), which is nonzero because \(k\) is real and \(m\omega>0\). Equation (2) has nonzero frequency \(m+1\), giving \(D\ge m+1\). Therefore **every** exponentially attracting realization satisfies \(\deg F\ge m+3\), and equality implies that \(k\) is constant.

When \(m=0\), \(h\) is constant and (1) says \(s=-kh\). Exponential attraction requires \(k\not\equiv0\) because its average is half the negative Floquet exponent. Then (2) reads \(e^{i\vartheta}(1-ih)k(\vartheta)\), whose highest positive Fourier order is at least one. Thus \(D\ge1\), so \(\deg F\ge3\). If equality holds, \(k\) must be constant here too. Since \(2k\) is the instantaneous normal linearization, degree-minimality forces pointwise constant radial damping, rather than assuming it in advance.

**4. Exact global attainment.** Fix any \(\kappa>0\). Let \(H(x,y)\) be the unique chosen polynomial obtained by replacing every \(\cos(j\vartheta)\) and \(\sin(j\vartheta)\) in the trigonometric polynomial
\[H(p(\vartheta))=\tfrac12\bigl(\kappa h(\vartheta)-\omega h'(\vartheta)\bigr)\tag{3}\]
with \(\operatorname{Re}(x+iy)^j\) and \(\operatorname{Im}(x+iy)^j\), respectively. Then \(\deg H=m\) for \(m\ge1\), and \(H\) is constant for \(m=0\). Define
\[\boxed{\ F(x,y)=\omega J(x,y)+(R-1)\left[-\frac\kappa2(x,y)+H(x,y)J(x,y)\right].\ }\tag{4}\]
For all \(r>0\), its polar equations are
\[\dot r=\frac\kappa2r(1-r^2),\qquad\dot\vartheta=\omega+(r^2-1)H(r\cos\vartheta,r\sin\vartheta).\]
The first equation shows that \(r(t)\to1\) from every \(r(0)>0\), monotonically and exponentially near the circle; no other nonconstant periodic orbit is possible. The origin is an equilibrium, all forward trajectories are bounded, and (4) is complete for forward time. On the circle, the nontrivial Floquet exponent is exactly \(-\kappa\). Its normal and angular derivatives are \(-\kappa\) and \(2H(p(\vartheta))\). By (3), the relation (1) holds with \(k=-\kappa/2\); hence \(Z=Jp+hp\) satisfies the periodic adjoint equation and the normalization \(Z\cdot F=\omega\). Uniqueness of the normalized periodic adjoint solution at a hyperbolic cycle identifies it with the actual asymptotic-phase gradient. The leading nonzero Fourier harmonic in \(H\) ensures \(\deg F=m+3\) when \(m\ge1\), and the radial cubic term ensures degree three when \(m=0\).

**5. Published fifth-harmonic target.** In [1, Sec. IV.3.1], with \(\omega=1\),
\[Z_*(\vartheta)=(-\sin(5\vartheta),\ 2\cos\vartheta-2\cos(3\vartheta)+\cos(5\vartheta)).\]
One computes \(Jp\cdot Z_*=1\) and \(p\cdot Z_*=2\sin(2\vartheta)-2\sin(4\vartheta)\). For \(\kappa=1\), let
\[H(x,y)=2xy-4xy(x^2-y^2)-2(x^2-y^2)+4(x^4-6x^2y^2+y^4).\]
Equation (4) with this \(H\) is an **explicit exact degree-seven** globally attracting realization of precisely the prescribed response \(Z_*\); the Fourier lower bound rules out every polynomial vector field of degree six or less satisfying the same orbital and phase-response specifications. This result does not assert that the numerical coefficients obtained in [1] equal (4).

## Verification

Run `python verify_degree.py` with SymPy installed. The script verifies exact polynomial radial and angular identities, the normalized adjoint equation modulo \(x^2+y^2-1\), the target Cartesian response from [1], and exact construction degree for eight further rational-coefficient harmonic inputs of degree zero through seven. It also constructs the complete 30-coefficient linear system for polynomial competitors of degree at most six for the published target; the coefficient matrix has rank 18 while its augmentation has rank 19, giving an independent exhaustive finite-dimensional obstruction in that example. The proof's lower bound uses an unrestricted Fourier-degree argument and **does not** follow from enumeration or numerical sampling. The packaged source code is self-contained apart from SymPy.

## Relationship to prior work

Namura, Ishii and Nakao [1] construct approximate polynomial oscillators by convex least squares and demonstrate the specific high-harmonic unit-circle phase response using a degree-seven polynomial. Their equations, methodology and numerical example were inspected. They do not state the general exact synthesis formula (4), the global attraction property for that realization, or a degree-minimality theorem. The present result supplies a precise reason why degree seven is necessary for the target they selected; their existence and synchronization demonstrations are fully credited.

Margalef-Bentabol and Peralta-Salas [2] prove polynomial realization for assigned cycle configurations, periods, multiplicities and stabilities. Those data do not fix an infinitesimal phase-response profile and therefore do not imply the Fourier-degree lower bound. Zeng [3] gives local closed-loop phase-field shaping under control authority assumptions, not sharp autonomous polynomial degree for a specified phase sensitivity. These are substantive neighboring results, not evidence of absolute priority; other constructions could conceivably contain an equivalent statement.

## Limitations

The minimum-degree claim concerns *one fixed physical-time circular trajectory* and a finite Fourier radial phase sensitivity. It does not determine the least polynomial degree for arbitrary noncircular curves, nontrigonometric responses, or phase response under time reparametrization. The global attraction statement concerns the constructed family, not all degree-minimal realizations. A matching identity in literature not found in the inspected sources could supersede the originality assessment. No independent mathematical audit has been performed.

## References

[1] N. Namura, T. Ishii and H. Nakao, *Designing two-dimensional limit-cycle oscillators with prescribed trajectories and phase-response characteristics*, arXiv:2301.07237, first public version 2023-01-18; see Sections III and IV.3. https://arxiv.org/abs/2301.07237

[2] J. Margalef-Bentabol and D. Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields*, arXiv:1507.00698, first public version 2015-07-02; Theorem 1.2. https://arxiv.org/abs/1507.00698

[3] S. Zeng, *Feedback design of isochron fields for nonlinear oscillators*, *Nonlinear Dynamics* (2026), published 2026-06-02, DOI:10.1007/s11071-026-12664-9. https://doi.org/10.1007/s11071-026-12664-9
