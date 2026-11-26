# Independent mathematical audit

## correctness

PASS

The alternating positive positions of 10101 require three windows, giving the universal upper bound. On four points let a,b,c be the successive differences and L,R the outer zero-gap lengths. The two alternating traces force a+b,b+c>=r+1 and L+a,R+c>=r. Those spans exclude any three queries in one window, so 1111 must split 2+2 and a,c<=r-1. Now 0000 can use only the gaps L,b-1,R: two must have length at least r or one must have length at least 2r. The two-gap cases give n>=3r+3, and the single-gap cases give n>=4r+2>3r+3. At equality the outer-outer case forces (L,a,b,c,R)=(r,1,r,1,r). The outer-middle case forces (r,1,r+1,c,r-c), or its reflection. In 0110 the two positive queries cannot share a window (their distance is at least r), so the interval strictly between the two excluded exterior queries must fit both windows. Its length is r+1 in the first case and r+1+c in the second, eliminating the first and forcing c=r-1 in the second. The affine witness table realizes all 16 traces for the reflected candidate, including r=2 and placements with adjacent windows, and the same placements embed in any larger chain. Independently, enumerating slack compositions before, between and after the windows and projecting the resulting binary strings tested 184191 supports for 2<=r<=8 from n=2r+1 through n=3r+3 and recovered exactly the two critical supports at each onset.

## originality

PASS

The strongest available comparators cover the VC upper bound of four for unrestricted unions of two intervals, or a single fixed-width window. They do not decide when exactly two disjoint copies of the same fixed-width integer interval can realize all four-point labelings, nor the equality classification for the smallest chain. The only exact indexed statement located is the assigned record itself. The pass is for the sharp restricted onset and rigidity, not the standard alternating-trace bound.

## value

PASS

On the natural fixed-width family, the general VC upper bound alone leaves open whether the length budget permits four fully independent responses. The exact threshold answers that question and the complete two-support rigidity identifies all optimally small query configurations, rather than one witness or an asymptotic estimate. The packing constraints distinguish the theorem from routine interval-class dimension bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
