# Independent mathematical audit

## correctness

PASS

On the four Boolean characters the eigenvalues are 0,2a,2b,2a+2b in the combinatorial normalization. Inverting the character transform gives strictly positive diagonal and original-edge entries for t>0 (C>A,B), and q/4 at one opposite position per row. For alpha<=1 the product (1-exp(-At))(1-exp(-Bt)) is a positive lower bound. For alpha>1 the sign of q' is that of a strictly increasing function starting at A+B-C<0 and tending to infinity, which proves the unique minimum and nonzero root using q(infinity)=1. Unit signed row sum gives the stated absolute row-sum norm. In scaled time the root satisfies tau=Lambda+log(phi(delta*tau)/phi(r^alpha*tau)) with phi(v)=integral_0^1 exp(-sv)ds. Strict decrease and exp(-v)<phi(v)<1 give the two strict bounds. At fixed alpha, delta=alpha*r+O(r^2) and the bracket width is O(r log(1/r)), giving the time and the log(alpha) offset. On compact scaled time intervals Q_r/r tends to -alpha*u*exp(-u), also in first derivative, so the already unique minimum tends to u=1 and its depth gives alpha*r/(2e) in the norm. For fixed a,b the linear and quadratic terms of q near order one are -2H(alpha-1)t and 4ab*t^2, with analytic higher terms. The implicit function theorem applied to q/t and q' gives t_alpha~H(alpha-1)/(2ab), a minimizing time half as large to first order, and peak coefficient H^2/(8ab), with the stated remainders. The bracket also squeezes the joint limit, including eta=0, since delta/r=alpha+O(r) uniformly near one. At t=0 the kernel is the identity; zero conductances are not within the theorem. Read CHECK.py and VERIFICATION.md; the reported 348 finite cases were not independently rerun and are not used as proof.

## originality

PASS

Pass for the unequal-rate classification and especially the strict anisotropic threshold bracket and weak-edge delay/vanishing peak law with its joint crossover. Credit the known unweighted square special case and the leading fixed-weight near-one coefficient supplied by a separate same-day weighted-graph theorem, without assuming date proves priority.

## value

PASS

This natural fixed-size anisotropic graph separates two operationally different stability measures: weak coupling makes the amplitude of the negative transient vanish linearly while its duration diverges logarithmically for every fixed superunit order. The sharp bracket, peak coefficient and near-one joint limit quantify the separation and its loss; the signed tail alone or the known unweighted result would not show this.

The dated certificate retains the supplied scientific assessment, sources and limitations.
