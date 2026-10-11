# Exact thermal broadening of the DM entanglement gap in a ferromagnetic XYZ dimer

## Finding

Consider the zero-field ferromagnetic XYZ dimer with a \(z\)-directed Dzyaloshinskii--Moriya coupling,
\[
J_z<J_y<J_x<0,\qquad D\ge0,\qquad T>0.
\]
Introduce
\[
A=\frac{J_x-J_y}{2}>0,\qquad
P=-\frac{J_x+J_y}{2}>0,\qquad
Z=-J_z>0,
\]
and
\[
\nu(D)=\sqrt{P^2+D^2}.
\]
The zero-temperature DM transition identified in the source occurs at
\[
\nu_c=A+Z,
\qquad
D_c=\sqrt{\nu_c^2-P^2}.
\]

At positive temperature, define
\[
u_+(T)
=
T\,\operatorname{arsinh}\!\left(
e^{Z/T}\cosh(A/T)
\right)
\]
and
\[
D_+(T)=\sqrt{u_+(T)^2-P^2}.
\]
For the lower edge, if
\[
e^{Z/T}\sinh(A/T)\le\cosh(P/T),
\]
set
\[
D_-(T)=0.
\]
Otherwise define
\[
u_-(T)
=
T\,\operatorname{arcosh}\!\left(
e^{Z/T}\sinh(A/T)
\right)
\]
and
\[
D_-(T)=\sqrt{u_-(T)^2-P^2}.
\]

Then the thermal concurrence vanishes exactly on one closed DM interval:
\[
\boxed{
C(T,D)=0
\quad\Longleftrightarrow\quad
D_-(T)\le D\le D_+(T).
}
\]
Equivalently, the concurrence is positive exactly for
\[
0\le D<D_-(T)
\]
or
\[
D>D_+(T).
\]

Whenever the left entangled region survives, so that
\[
D_-(T)>0,
\]
the source's zero-temperature transition point lies strictly inside the thermal gap:
\[
\boxed{
D_-(T)<D_c<D_+(T).
}
\]

The low-temperature broadening is exponentially narrow. As
\[
T\downarrow0,
\]
\[
D_c-D_-(T)
\sim
\frac{\nu_c}{D_c}\,T e^{-2A/T},
\]
and
\[
D_+(T)-D_c
\sim
\frac{\nu_c}{D_c}\,T e^{-2A/T}.
\]
Therefore
\[
\boxed{
D_+(T)-D_-(T)
\sim
\frac{2\nu_c}{D_c}\,T e^{-2A/T}.
}
\]

Thus the positive-temperature zero-concurrence interval described qualitatively in the source has exact analytic edges. Its birth from the single zero-temperature critical point is asymptotically symmetric in \(D\) to leading order, with an exponentially small width controlled by the anisotropy scale \(A=(J_x-J_y)/2\).

For example, for
\[
J_x=-1,\qquad J_y=-2,\qquad J_z=-3,
\]
one has
\[
A=\frac12,\qquad P=\frac32,\qquad Z=3,
\qquad
D_c=\sqrt{10}.
\]
At
\[
T=0.2,
\]
the exact edges are approximately
\[
D_-=3.1607810394,
\qquad
D_+=3.1637641018,
\]
while
\[
D_c=3.1622776602.
\]

## Assumptions and scope

The result concerns the zero-field ferromagnetic XYZ sector treated in the source:
\[
J_z<J_y<J_x<0.
\]
The DM coupling is taken nonnegative because the concurrence depends on it through
\[
\nu(D)=\sqrt{P^2+D^2}.
\]
Units are chosen so that Boltzmann's constant is one.

The statement classifies the zero versus positive two-qubit concurrence for this thermal family. It does not concern multipartite systems, nonuniform fields, other orientations of the DM vector, or entanglement measures other than concurrence.

The low-temperature asymptotic assumes fixed couplings satisfying the strict ferromagnetic ordering above.

## Proof

In the source notation,
\[
J_+=\frac{J_x+J_y}{2}=-P,
\qquad
J_-=\frac{J_x-J_y}{2}=A,
\qquad
J_z=-Z.
\]
Its ferromagnetic zero-temperature transition is determined by
\[
\sqrt{J_+^2+D_c^2}
=
J_- - J_z
=
A+Z
=
\nu_c.
\]
Hence
\[
D_c=\sqrt{\nu_c^2-P^2}.
\]

For the undercritical branch
\[
D<D_c,
\]
the source gives
\[
C_-(T,D)
=
\max\!\left\{
\frac{
\sinh(A/T)
-
e^{-Z/T}\cosh(\nu/T)
}{
\cosh(A/T)
+
e^{-Z/T}\cosh(\nu/T)
},
0
\right\}.
\]
The denominator is positive, and \(\nu(D)\) is strictly increasing in \(D\). Therefore
\[
C_-(T,D)>0
\]
exactly when
\[
\cosh(\nu/T)
<
e^{Z/T}\sinh(A/T).
\]
If the right-hand side does not exceed
\[
\cosh(P/T),
\]
then this inequality fails even at \(D=0\), and the entire undercritical branch has zero concurrence. This is precisely the case in which we set
\[
D_-(T)=0.
\]

Otherwise there is a unique solution
\[
u_-(T)
=
T\,\operatorname{arcosh}\!\left(
e^{Z/T}\sinh(A/T)
\right),
\]
and the undercritical concurrence is positive exactly for
\[
\nu(D)<u_-(T),
\]
or equivalently
\[
D<D_-(T).
\]

Moreover,
\[
e^{Z/T}\sinh(A/T)
<
\cosh((A+Z)/T),
\]
because
\[
\cosh((A+Z)/T)
-
e^{Z/T}\sinh(A/T)
=
\frac12
\left(
e^{-(A+Z)/T}
+
e^{(Z-A)/T}
\right)
>0.
\]
Hence, whenever \(u_-\) exists,
\[
u_-(T)<\nu_c,
\]
and therefore
\[
D_-(T)<D_c.
\]

For the overcritical branch
\[
D>D_c,
\]
the source gives
\[
C_+(T,D)
=
\max\!\left\{
\frac{
\sinh(\nu/T)
-
e^{Z/T}\cosh(A/T)
}{
\cosh(\nu/T)
+
e^{Z/T}\cosh(A/T)
},
0
\right\}.
\]
Again the denominator is positive and the numerator is strictly increasing in \(\nu\). Thus
\[
C_+(T,D)>0
\]
exactly when
\[
\nu(D)>u_+(T),
\]
where
\[
u_+(T)
=
T\,\operatorname{arsinh}\!\left(
e^{Z/T}\cosh(A/T)
\right).
\]
At \(\nu=\nu_c=A+Z\),
\[
e^{Z/T}\cosh(A/T)
-
\sinh((A+Z)/T)
=
\frac12
\left(
e^{(Z-A)/T}
+
e^{-(A+Z)/T}
\right)
>0,
\]
so
\[
u_+(T)>\nu_c
\]
and therefore
\[
D_+(T)>D_c.
\]

Combining both source branches with
\[
C(T,D_c)=0
\]
gives the exact interval
\[
C(T,D)=0
\quad\Longleftrightarrow\quad
D_-(T)\le D\le D_+(T).
\]

For the low-temperature width, write
\[
\delta_-(T)=\nu_c-u_-(T),
\qquad
\delta_+(T)=u_+(T)-\nu_c.
\]
The lower-edge equation can be written exactly as
\[
e^{-\delta_-/T}
\left(
1+e^{-2u_-/T}
\right)
=
1-e^{-2A/T}.
\]
Therefore
\[
\frac{\delta_-}{T}
=
\log\!\left(1+e^{-2u_-/T}\right)
-
\log\!\left(1-e^{-2A/T}\right).
\]
Since
\[
\nu_c=A+Z>A,
\]
the first exponential is of smaller order than
\[
e^{-2A/T},
\]
and consequently
\[
\delta_-(T)
\sim
T e^{-2A/T}.
\]

Similarly, the upper-edge equation yields
\[
e^{\delta_+/T}
\left(
1-e^{-2u_+/T}
\right)
=
1+e^{-2A/T},
\]
so
\[
\frac{\delta_+}{T}
=
\log\!\left(1+e^{-2A/T}\right)
-
\log\!\left(1-e^{-2u_+/T}\right),
\]
and hence
\[
\delta_+(T)
\sim
T e^{-2A/T}.
\]

Finally,
\[
D(\nu)=\sqrt{\nu^2-P^2}
\]
has derivative
\[
D'(\nu_c)=\frac{\nu_c}{D_c}.
\]
Applying this first-order expansion to \(u_-\) and \(u_+\) proves both one-sided asymptotics and the stated gap-width law.

## Verification

`verify_ferro_xyz_dm_gap.py` evaluates the two source concurrence branches directly.

For deterministic ferromagnetic parameter sets and temperatures, it checks that the sign of the source concurrence agrees with the closed interval classification, verifies
\[
D_-<D_c<D_+,
\]
whenever the lower edge is positive, and checks the exact threshold equations defining both edges.

It also verifies convergence of the normalized low-temperature width
\[
\frac{D_+(T)-D_-(T)}
{(2\nu_c/D_c)\,T e^{-2A/T}}
\]
to \(1\).

The finite replay is supplementary. The all-parameter interval classification and low-temperature asymptotic are supplied by the analytic proof above.

## Relationship to prior work

Gürkan and Pashaev derive the ferromagnetic XYZ concurrence on separate undercritical and overcritical DM branches. They identify the zero-temperature critical coupling
\[
\sqrt{J_+^2+D_c^2}=J_- - J_z
\]
and state that, for positive temperature, entanglement vanishes on an interval containing \(D_c\) whose extent grows with temperature.

The exact two edge formulas above turn that qualitative interval into a closed analytic phase boundary. They also show that the interval born from the zero-temperature critical point is exponentially narrow as \(T\downarrow0\), with the same leading displacement on both sides.

The earlier arXiv treatment by the same authors studies the general XYZ chain with DM interaction and contains the same model family. The later journal article consolidates the analysis and explicitly presents the two finite-temperature concurrence branches used here.

Related two-qubit XXZ and XYZ work with DM coupling studies thermal entanglement, critical temperatures, and field effects, but targeted searches did not locate these exact ferromagnetic XYZ interval edges or the
\[
T e^{-2A/T}
\]
broadening law.

## Limitations

The exact gap formula is specific to the zero-field ferromagnetic ordering
\[
J_z<J_y<J_x<0
\]
and a \(z\)-directed DM coupling.

The result quantifies the concurrence-zero interval; it does not claim a thermodynamic phase transition at positive temperature.

The interval width is asymptotically symmetric only to leading order. The two edge corrections differ at smaller exponential orders.

A residual literature risk remains because the source family has been studied under several equivalent coupling conventions, and an algebraically equivalent edge formula may exist in unindexed literature.

## References

1. Z. N. Gürkan and O. K. Pashaev, “Two Qubit Entanglement in Magnetic Chains with DM Antisymmetric Anisotropic Exchange Interaction,” arXiv:0804.0710, first submitted 4 April 2008.
2. Z. N. Gürkan and O. K. Pashaev, “Entanglement in two qubit magnetic models with DM antisymmetric anisotropic exchange interaction,” *International Journal of Modern Physics B* 24 (2010), 943–965, DOI: 10.1142/S0217979210054579.
3. Z. N. Gürkan and O. K. Pashaev, “Two Qubit Entanglement in \(XYZ\) Magnetic Chain with DM Antisymmetric Anisotropic Exchange Interaction,” arXiv:0705.0679, first submitted 7 May 2007.
