# Independent mathematical audit

## correctness

PASS

Given a new table born when root table occupancy is r, later two-table choices form classical Polya urn (r,1); eventual challenger victory probability h_r=Pr(Beta(1,r)>1/2)=2^-r. Ever strict takeover integrates biased gambler ruin over Beta to g_r=2^-r+r int_0^(1/2) x^r/(1-x)dx, bounded by 2^(1-r). Birth at fixed time j has probability epsilon=1-p and R_(j-1)->j-1 as p->1; two fixed births contribute at most epsilon^2. Need control infinite late-birth union: on no-early-birth history root starts J and couples below by independent Bernoulli J/(2n), giving E 2^-R_n<=2^-J(J/n)^(J/4) and exponential J tail; histories with early births have probability O_J(epsilon) and their conditional late-challenger risk ->0 by finite-state convergence to positive-root-share Polya at p=1. Thus exchanging first-order limit with infinite union is justified. A finite-family squeeze avoids interchanging max over infinitely many tables with n-limit for theta. Summing h_r=1 and sum (g_r-h_r)=1/2 proves slopes. Independent direct series yields g_1=ln2, g_2=0.386294361..., sum g=1.5; not a replacement for late-birth lemma. First-time ties favor root, so strict takeover is correct failure event.

## originality

PASS

Zheng arXiv:2606.01881 studies the identical root-leadership model and proves positivity, monotonicity, continuity and existence of theta, so these facts are prior; available primary abstract and detailed external descriptions do not report endpoint derivatives. Baur arXiv:1407.2508 treats joint n->infinity, p(n)->1 large-cluster asymptotics and is not the requested iterated slope. Complete Zheng primary PDF was inaccessible via arXiv/OA and authorized institutional access returned vpn_disconnected, so its full theorem set could contain stronger overlap; this is an explicit serious residual risk, NOT invented NOT_COVERING. Bounded best-knowledge novelty of exact unequal slopes remains.

## value

PASS

Eventual leadership and eternal leadership are two canonical non-equivalent events in random recursive tree percolation. Their sharp unequal first-order constants quantitatively isolate temporary defeat and recovery, requiring subtle tail control of infinitely many challenger births; this is a motivated probabilistic invariant and not a finite toy calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
