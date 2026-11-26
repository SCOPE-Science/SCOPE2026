# Independent mathematical audit

## correctness

PASS

Counting (y,z) base values with multiplicity in residue dr gives D(n) by a prefix count, so g_p is max_r(T_r−a) for the (p+1)st base T_r. The rows y+2z=r+ka have step a, lengths floor((r+ka)/2)+1 and starts a ceil((r+ka)/2)+d(r+ka). These formulas reproduce the frozen parity inequalities. With U=a(p+m)+(2a−1)d, rows 0–1 already suffice when p<K_r; otherwise their entries lie below U and row 2 supplies the missing counts. This does not sort the rows globally. In r=a−1, row 1 reaches U and row 2 starts U+a(a+d−p), so exactly p entries precede U, even at the tie p=a+d. At p₀=a+d+1, lower U by a−2d. Rows 0–1 plus the first needed row-2 entries work when p₀≥K_r. When p₀<K_r at most one of the previously counted row-1 entries exceeds the reduced threshold (the reduction is strictly less than the step a), and L₂(r) is below the threshold by at least 2d. For r=1, the reduced threshold is the relevant row-2 entry and L₃(1) is one full step above it; the immediately preceding residue point has at most p₀ entries. This gives equality and the change from residue −d to d. Coprimality makes a=2d impossible. Independently checked all 2817 levels and their maximizer residues across 147 coprime pairs via direct base histogram and residue prefix sums, with a terminal block of a consecutive counts exceeding p₀ to certify each finite tail.

## originality

PASS

The strongest distinct same-day result gives the adjacent level p=m+1 for d≥3 and agrees there with extrapolating the affine expression, but does not give any of the frozen levels or the first break. The prior d=1 analogue and general denumerant or Apéry machinery do not give this uniform d≥2 phase and its exact endpoint.

## value

PASS

This is an exact threshold classification across an interval whose length grows with the parameters, in a standard arithmetic-progression family with a known low-p theory. It identifies a change of the controlling residue and the first departure from linearity, information not furnished by an isolated next level, eventual growth, or bounded enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
