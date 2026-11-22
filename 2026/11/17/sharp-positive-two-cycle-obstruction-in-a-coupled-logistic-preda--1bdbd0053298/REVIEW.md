# Independent mathematical audit

## correctness

PASS

For every strictly positive least-period-two orbit, positivity of prey x forces 0<x_i<1. Adding the normalized prey and predator update equations yields S_x<2(a−1)/a and S_y<2(b+d−1)/b. Arithmetic-harmonic inequalities imply R_x>a when a≤3 and R_y>b when b+d≤3, including weak endpoints because c,d>0. Subtracting yields (R_x−a)Δx=cΔy and (R_y−b)Δy=−dΔx, whose strictly positive determinant (R_x−a)(R_y−b)+cd forces Δx=Δy=0. At a or b just above 3, scalar f_r(u)=ru(1−u) has hyperbolic attracting primitive two-cycle for 3<r<1+sqrt(6), which continues by IFT to small c=d>0 while the other coordinate stays logistic fixed at 1/2. Inspected actual checker.py confirms normalized identities symbolically; external independent SymPy symbolic subtraction reproduced them. The theorem does not require global positive-quadrant invariance.

## originality

PASS

The accessible 2024 same-map coupled-logistic research treats local fixed point stability and flip bifurcations; these cannot by themselves rule out an arbitrary disconnected strictly positive primitive two-cycle. The older 2018 applied-mathematics paper may contain more global bifurcation analysis; no lawful public full text was obtainable and authorized institutional access reported vpn_disconnected, making it a named priority risk rather than automatic failure. Related Resultary plankton exclusion theorems have different predator equations and neither imply the exact coordinatewise rectangle a≤3,b+d≤3. Best-of-knowledge PASS.

## value

PASS

A sharp two-coordinate universal exclusion region for all positive states is a meaningful global restriction beyond local bifurcation calculations, with explicit hyperbolic existence arbitrarily near either parameter boundary. It explains which numerical 2-cycle observations require threshold exceedance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
