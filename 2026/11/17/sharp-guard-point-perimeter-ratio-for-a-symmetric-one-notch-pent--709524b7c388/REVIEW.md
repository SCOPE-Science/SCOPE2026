# Independent mathematical audit

## correctness

PASS

Reconstructed the inward halfplane kernel inequalities after vertical scaling, including both b<=t/(1-t) and b>t/(1-t) chambers and the boundary switch, then integrated twice the halfwidth to obtain the stated piecewise rational kernel-area expression. The polygon area is h[1+b(1-t)], hull perimeter 2(1+b+sqrt(h²+(1-b)²)) and notched perimeter 2(1+sqrt(h²+(1-b)²)+sqrt(t²h²+b²)). The strict finite-height inequality N-b<h<1+b+L yields G/P<(1+t)k/[1+b(1-t)], with equality approached only h→infinity. Exact derivative in b has one sign change at b=t(1+sqrt2)/(1-t); substituting produces H(t), whose derivative is minus a strictly increasing cubic over a positive denominator. Thus one t* in (0,1) uniquely maximizes H. Independently factored both rational derivatives, branch continuity and the cubic and reproduced 1.0260783949639667. Claims are strictly for the specified family, not all pentagons.

## originality

PASS

This is an exact constrained-family solution to a symmetric notch optimization, not a new global best counterexample. Nakano provides G<=2P and a qualitative pentagon counterexample; Baker gives a larger unrestricted lower bound >1.061 and open one-notch tasks. Neither an upper bound or a global lower bound implies the exact 1.026... constrained maximum, unique limiting parameters or nonattainment. Full Nakano/Baker/Sibley reading was blocked; this is a best-of-knowledge verdict with meaningful priority risk.

## value

PASS

The one-notch centered symmetric family is naturally singled out in prior guard-point/perimeter questions; exactly classifying its sharp constant, optimizer and nonattainment constrains and calibrates broader polygon optimization. This is not a trivial tiny witness nor a new unrestricted record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
