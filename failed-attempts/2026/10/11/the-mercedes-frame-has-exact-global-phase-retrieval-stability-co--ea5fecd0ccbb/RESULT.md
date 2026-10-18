# The Mercedes frame has exact global phase-retrieval stability constant \(\sqrt{2}\)
## Finding
Let
\[
u_0=(1,0),\qquad
u_1=\left(-\frac12,\frac{\sqrt3}{2}\right),\qquad
u_2=\left(-\frac12,-\frac{\sqrt3}{2}\right)
\]
be the unit-norm Mercedes frame in \(\mathbb{R}^2\), and let \(\Theta x=(\langle x,u_k\rangle)_{k=0}^2\). For the quotient metric
\[
d_{\pm}(x,y)=\min_{\varepsilon\in\{-1,1\}}\|x-\varepsilon y\|_2,
\]
the smallest constant \(C\) satisfying
\[
d_{\pm}(x,y)\le C\,\big\||\Theta x|-|\Theta y|\big\|_2
\qquad\text{for all }x,y\in\mathbb{R}^2
\]
is
\[
C=\sqrt2.
\]
Equivalently, the sharp global lower Lipschitz constant of the magnitude analysis map is \(1/\sqrt2\).

## Assumptions and scope
The field is real, the three Mercedes vectors have unit norm, and both the signal and measurement spaces use their Euclidean norms. The phase ambiguity is therefore the sign ambiguity \(\{\pm1\}\). The 2022 stability theorem of Alharbi--Alshabhi--Freeman--Ghoreishi reduces the worst global stability ratio to orthogonal signal pairs, which is the only non-elementary input used below.

## Proof
By the orthogonal-pair reduction, it is enough to consider \(x\perp y\). Write
\[
x=r(\cos\theta,\sin\theta),\qquad
y=s(-\sin\theta,\cos\theta),\qquad r,s\ge0.
\]
For \(\alpha_k=2\pi k/3\), the \(k\)-th Mercedes coefficient magnitudes are
\[
r|\cos(\theta-\alpha_k)|
\quad\text{and}\quad
s|\sin(\theta-\alpha_k)|.
\]
Thus, if
\[
D=\big\||\Theta x|-|\Theta y|\big\|_2,
\]
then
\[
D^2
=\frac32(r^2+s^2)-rsL(2\theta),
\]
where
\[
L(t)=|\sin t|+|\sin(t+2\pi/3)|+|\sin(t+4\pi/3)|.
\]
The function \(L\) has period \(\pi/3\). On \(0\le t\le\pi/3\), the signs are fixed and
\[
L(t)=\sin t+\sin(t+2\pi/3)-\sin(t+4\pi/3)
      =\sin t+\sqrt3\cos t
      =2\sin(t+\pi/3)\le2.
\]
Therefore
\[
D^2\ge\frac32(r^2+s^2)-2rs
     =\frac12(r^2+s^2)+(r-s)^2
     \ge\frac12(r^2+s^2).
\]
Since \(x\perp y\), both \(\|x-y\|_2\) and \(\|x+y\|_2\) equal \(\sqrt{r^2+s^2}\). Hence
\[
d_{\pm}(x,y)\le\sqrt2\,D,
\]
so the global stability constant is at most \(\sqrt2\).

Sharpness is attained by
\[
x=\frac{(1,1)}{\sqrt2},\qquad
y=\frac{(-1,1)}{\sqrt2}.
\]
These vectors are orthogonal and have unit norm. Their three absolute coefficient differences are
\[
0,\qquad \frac1{\sqrt2},\qquad \frac1{\sqrt2},
\]
so \(D=1\), while \(d_{\pm}(x,y)=\sqrt2\). Therefore no smaller constant is possible.

## Verification
Every step after the orthogonal-pair reduction is an exact trigonometric identity. The periodic reduction of \(L\), its maximum \(2\), and the equality witness are symbolic. No numerical experiment is used to infer the global statement. The Mercedes frame is \(3/2\)-tight, and the equality pair realizes the exact lower Lipschitz ratio \(1/\sqrt2\).

## Relationship to prior work
Alharbi--Alshabhi--Freeman--Ghoreishi prove that the worst stability inequality for phase retrieval is witnessed at orthogonal vectors, making the exact optimization above possible. Bandeira--Cahill--Mixon--Nelson give general real phase-retrieval stability bounds through the strong complement property, but those general bounds do not themselves evaluate this frame-specific optimum. Bodmann--Casazza--Edidin--Balan use the same three-vector real equiangular tight frame as the Mercedes-Benz frame in phase-retrieval reconstruction, establishing the object as a canonical example rather than an ad hoc configuration.

## Limitations
The exact constant here is for the real, unit-norm Mercedes frame and Euclidean magnitude measurements. It does not assert the same constant for complex phase retrieval, other measurement norms, reweighted or rescaled Mercedes systems, or arbitrary three-vector frames. Multiplying every frame vector by a common positive scalar multiplies the lower Lipschitz constant by that scalar and divides the stability constant by it.

## References
1. W. Alharbi, S. Alshabhi, D. Freeman, and D. Ghoreishi, *Locality and stability for phase retrieval*, arXiv:2210.03886v1, 2022.
2. A. S. Bandeira, J. Cahill, D. G. Mixon, and A. A. Nelson, *Saving phase: Injectivity and stability for phase retrieval*, arXiv:1302.4618, 2013.
3. B. G. Bodmann, P. G. Casazza, D. Edidin, and R. Balan, *Frames for linear reconstruction without phase*, CISS 2008, DOI 10.1109/CISS.2008.4558616.
