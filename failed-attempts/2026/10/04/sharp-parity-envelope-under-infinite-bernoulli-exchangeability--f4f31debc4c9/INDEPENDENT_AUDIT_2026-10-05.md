# Independent mathematical audit

## correctness

PASS

De Finetti reduces the parity bias exactly to \(\mathbb E M^n\) for a random \(M\in[-1,1]\) with fixed mean. For even \(n\), Jensen and the endpoint mixture give the exact lower and upper moments. For odd \(n\), the tangent at \(-c_n\) satisfying \(c_n^{n-1}(n+(n-1)c_n)=1\) joins \((-c_n,-c_n^n)\) to \((1,1)\); its derivative comparison proves that the piecewise curve is the least concave majorant, and reflection gives the greatest convex minorant. The stated two-atom laws attain the endpoints, mixtures interpolate, and the defining equation yields the fair-marginal limit. Fresh numerical envelope checks for every odd \(3\le n<30\) corroborated the proof.

## originality

FAIL

The scientific reduction is a standard one-moment extremal problem. A general published upper-concave-envelope identity states \((\mathfrak C f)(x)=\sup_{V:\,EV=x}E f(V)\), and the already-published SCOPE extendible-Bernoulli tail result explicitly uses the same de Finetti-plus-least-concave-majorant mechanism and labels the one-fixed-moment identity standard. Once parity is written as \(f(M)=M^n\), the submitted theorem is exactly that general identity plus an elementary calculation of the envelope of a monomial. The tangent equation and two-atom law are therefore a direct specialization of a stronger standard framework, despite not being printed with the same parity notation.

## value

FAIL

The parity interval is a neat closed-form example, but after the standard de Finetti reduction and the general fixed-mean concave-envelope theorem, the only remaining step is the elementary tangent construction for \(x^n\). Under the common value bar that is a worked specialization of a stronger framework rather than a new structural gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
