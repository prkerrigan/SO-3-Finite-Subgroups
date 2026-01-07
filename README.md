# Translation Guide: main.tex to main_vi.tex

This document describes the line-by-line translation between the English version (main.tex) and Vietnamese version (main_vi.tex) of the paper "Visualizing Rotations of Space and its Finite Subgroups".

## Preamble Differences (Lines 1-20)

| Lines | main.tex | main_vi.tex | Notes |
|-------|----------|-------------|-------|
| 1 | `\documentclass{article}` | `\documentclass{article}` | Same |
| 2 | `\usepackage{maa-monthly}` | `\usepackage[utf8]{inputenc}` | Vietnamese version adds UTF-8 encoding |
| 3 | `\usepackage{patrick_custom}` | `\usepackage[T1]{fontenc}` | Vietnamese version adds font encoding |
| 4 | `\usepackage{subcaption, tikz-cd}` | `\usepackage{vntex}` | Vietnamese version adds Vietnamese TeX support |
| 5-8 | Font comments (same) | Same packages as English version | Vietnamese version reorders packages |
| 13-14 | `\newtheorem{theorem}{Theorem}` | `\newtheorem{theorem}{Định lý}` | "Theorem" → "Định lý" |
| 16-17 | `\newtheorem*{definition}{Definition}` and `\newtheorem*{remark}{Remark}` | `\newtheorem*{definition}{Định nghĩa}` and `\newtheorem*{remark}{Nhận xét}` | "Definition" → "Định nghĩa", "Remark" → "Nhận xét" |

## Title and Abstract (Lines 22-30)

| Lines | main.tex | main_vi.tex | Translation |
|-------|----------|-------------|-------------|
| 22 | `\title{Visualizing Rotations of Space and its Finite Subgroups}` | `\title{Trực quan hóa các phép quay không gian và các nhóm con hữu hạn của nó}` | Title translated to Vietnamese |
| 23 | `\markright{Rotations and its Finite Subgroups}` | `\markright{Các phép quay và các nhóm con hữu hạn}` | Running head translated |
| 28-30 | Abstract in English about finite subgroups and Platonic solids | Abstract in Vietnamese with similar content | Full abstract translated, emphasizes conjugacy classes and polyhedra relationship |

## Introduction Section (Lines 33-264)

### Key Translation Points:

| English Line | Vietnamese Line | Key Translations |
|--------------|-----------------|------------------|
| 35 | 38 | "finite subgroups of spacial rotations" → "các nhóm con hữu hạn của các phép quay không gian" |
| 41 | 44 | "cyclic groups of order k" → "các nhóm cyclic bậc k" |
| 42 | 45 | "dihedral groups of order 2k" → "các nhóm dihedral bậc 2k" |
| 46 | 49 | "alternating group on 4 elements" → "nhóm xen kẽ trên 4 phần tử" |
| 51-53 | 54-60 | "principle homogeneous space" → "không gian thuần nhất chính" |
| 52 | 55 | "$G$-torsor" remains same, definition translated |
| 58 | 61 | "axis-angle representation" → "biểu diễn trục-góc" |
| 82 | 85 | "Lie algebra" → "đại số Lie" (technical term kept) |
| 83 | 86 | "Lie bracket or commutator" → "tích Lie" (simplified in Vietnamese) |
| 92 | 95 | "infinitesimal structure" → "cấu trúc vô cùng nhỏ" |
| 94-101 | 97-104 | "Exponential map" definition → "Ánh xạ mũ" |
| 113 | 116 | Compactness and connectedness statement (same mathematical content) |
| 130-134 | 133-137 | "quotient map" → "ánh xạ thương" |
| 135 | 138 | "quotient topology" → "tô pô thương" |
| 142 | 145 | "homeomorphism" → "phép đồng phôi" |
| 157 | 160 | "gluing" → "việc dán", "cut" or "flattened" → "cắt" or "làm phẳng" |

### Definition Boxes:

| English Line | Vietnamese Line | Term |
|--------------|-----------------|------|
| 52-56 | 55-59 | Definition of $G$-torsor / principle homogeneous space |
| 94-101 | 97-104 | Definition of Exponential map |
| 198-208 | 201-211 | Definition of Preimage and Image |

### Theorem 1 (Lines 238-258 → Lines 241-261):

- **Line 238/241**: "Theorem" → "Định lý"
- **Content**: Mathematical statement remains identical (formula-based)
- **Proof label**: "proof" implied in both, "Proof" → "Chứng minh" implied

## Derived Polyhedra Section (Lines 266-400)

| English Line | Vietnamese Line | Key Translations |
|--------------|-----------------|------------------|
| 266 | 269 | "Derived Polyhedra" → "Các khối đa diện dẫn xuất" |
| 268-273 | 271-276 | "0-cell" → "0-ô", "n-cell" → "n-ô" |
| 274 | 277 | "2-CW complex" → "phức CW 2 chiều" |
| 279-280 | 282-283 | "Regularity" definition → "Tính đều đặn" |
| 282-290 | 285-293 | "Adjacent cells and shells" → "Các ô liền kề và vỏ" |
| 294 | 297 | "vertices" → "các đỉnh" |
| 295 | 298 | "edges" → "các cạnh" |
| 306 | 309 | "faces" → "các mặt" |
| 315-320 | 318-323 | Properties labeled with references (\ref{pbd}, \ref{cinv}, \ref{eucha}) |
| 330-331 | 333-334 | "Similar cells" definition → "Các ô tương tự" |
| 333-339 | 336-342 | "Similar cells have similar shells" theorem → "Các ô tương tự có vỏ tương tự" |
| 348-350 | 351-352 | "Derived polyhedron" definition → "Khối đa diện dẫn xuất" |

### Mathematical Structures Preserved:

- Equations and formulas remain identical in both versions
- Theorem numbering and referencing maintained
- CW complex notation preserved
- Group theory symbols unchanged (e.g., $G$, $SO(3)$, $\R^3$)

## Cyclic and Dihedral Groups Section (Lines 401-419)

| English Line | Vietnamese Line | Key Translations |
|--------------|-----------------|------------------|
| 401 | 404 | "Cyclic and Dihedral groups" → "Các nhóm cyclic và dihedral" |
| 403-409 | 406-412 | Figure caption and description translated |
| 407 | 410 | Figure label preserved: `\label{fig:D5inSO3}` |
| 408 | 411 | "Unfilled stars" → "Các ngôi sao không tô màu" |
| 411 | 414 | "class equation" → Reference to class equation (content simplified) |
| 413 | 416 | "group elements" → "các phần tử nhóm" |
| 413 | 416 | "2-cycles" → "các phép lật" (flips) |
| 415 | 418 | "5-cycles" → "5-chu trình" |

## Alternating and Symmetric Groups Section (Lines 420-503)

| English Line | Vietnamese Line | Key Translations |
|--------------|-----------------|------------------|
| 420 | 423 | "Alternating and Symmetric groups" → "Các nhóm xen kẽ và đối xứng" |
| 421 | 424 | Discussion of $S_4$ and symmetries |
| 423-451 | 426-454 | Figure 2 with four subfigures showing different views of $S_4$ |
| 442-448 | 445-451 | Table mapping conjugacy classes to polyhedra shapes |
| 461-489 | 464-492 | Figure 3 showing $A_5$ with subfigures |
| 479-486 | 482-489 | Table for $A_5$ conjugacy classes |
| 491-496 | 494-499 | Discussion of $A_4$ as subgroup of $S_4$ |

### Color-Coded Polyhedra Tables:

**For $S_4$ (Lines 443-447 → 446-450):**
- "red octahedron" → "bát diện đỏ" (4-cycles)
- "blue cube" → "hình lập phương xanh" (3-cycles)
- "yellow octahedron" → "bát diện vàng" (2-2-cycles)
- "green cuboctahedron" → "khối lập phương bát diện xanh lá" (2-cycles)

**For $A_5$ (Lines 481-485 → 484-488):**
- "red icosahedron" → "icosahedron đỏ" (5-cycles, k=1)
- "blue dodecahedron" → "dodecahedron xanh" (3-cycles)
- "green icosahedron" → "icosahedron xanh lá" (5-cycles, k=2)
- "yellow icosidodecahedron" → "icosidodecahedron vàng" (2-2-cycles)

## Conclusions Section (Lines 505-507)

| English Line | Vietnamese Line | Key Translations |
|--------------|-----------------|------------------|
| 505 | 508 | "Conclusions" → "Kết luận" |
| 505-506 | 508-514 | Significantly expanded Vietnamese conclusion |

**English version** (2 lines): Brief summary about geometry of finite groups and visualizations without calculations.

**Vietnamese version** (7 additional lines): Extended conclusion that includes:
- Relationship between group geometry and object geometry
- Axis-angle representation explanation
- Discussion of derived polyhedra concept
- Suggestions for higher-dimensional exploration

## Bibliography (Lines 508-511)

| English Line | Vietnamese Line | Content |
|--------------|-----------------|---------|
| 509-511 | 515-517 | Bibliography commands identical |

## Key Translation Patterns

### 1. **Technical Mathematical Terms:**
- "Lie algebra" → "đại số Lie"
- "exponential map" → "ánh xạ mũ"
- "homeomorphism" → "phép đồng phôi"
- "quotient space" → "không gian thương"
- "conjugacy class" → "lớp liên hợp"
- "torsor" → kept as "torsor" (technical term)

### 2. **Geometric Objects:**
- "tetrahedron" → "tứ diện"
- "cube" / "hexahedron" → "hình lập phương" / "lục diện"
- "octahedron" → "bát diện"
- "dodecahedron" → "dodecahedron" (kept Greek origin)
- "icosahedron" → "icosahedron" (kept Greek origin)
- "polyhedron" → "khối đa diện"

### 3. **Group Theory Terms:**
- "cyclic group" → "nhóm cyclic"
- "dihedral group" → "nhóm dihedral"
- "alternating group" → "nhóm xen kẽ"
- "symmetric group" → "nhóm đối xứng"
- "order" (of group) → "bậc"
- "subgroup" → "nhóm con"

### 4. **Common Mathematical Phrases:**
- "for example" → "ví dụ"
- "that is" → "tức là"
- "we have" → "chúng ta có"
- "consider" → "xét"
- "proof" → "chứng minh"

### 5. **Document Structure Terms:**
- "Theorem" → "Định lý"
- "Definition" → "Định nghĩa"
- "Remark" → "Nhận xét"
- "Figure" → "Hình"
- "Section" → preserved in commands but content translated

## Notable Structural Differences

1. **Package Loading Order**: Vietnamese version loads font and encoding packages first (lines 2-4 in main_vi.tex)

2. **Abstract Length**: Vietnamese abstract (lines 31-33) is more concise than English (lines 28-30)

3. **Explanatory Text**: Some English explanations are streamlined in Vietnamese, while the conclusion section is expanded

4. **Mathematical Content**: All equations, formulas, theorem statements, and proofs are identical in both versions

5. **Figure References**: All figure labels and references are preserved identically (e.g., `\ref{fig:D5inSO3}`, `\ref{fig:s4}`)

6. **Citation Style**: Bibliography style and citations maintained identically (e.g., `\cite{klein}`, `\cite{hall}`)

## Line Count Summary

- **main.tex**: 513 lines
- **main_vi.tex**: 519 lines
- **Difference**: +6 lines in Vietnamese version (primarily in conclusion section)

## Usage Notes

- Both files use the same custom packages: `maa-monthly` and `patrick_custom`
- Both reference the same `references.bib` file
- All figures referenced from the `figures/` directory
- Mathematical notation and symbols remain unchanged between versions
- The Vietnamese version requires `vntex` package for proper Vietnamese text rendering
