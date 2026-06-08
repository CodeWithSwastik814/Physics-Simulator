from manim import *

# ─────────────────────────────────────────────
#  Color palette
# ─────────────────────────────────────────────
BG       = "#0d0d1a"
ACCENT1  = "#00e5ff"   # cyan
ACCENT2  = "#ff6b35"   # orange
ACCENT3  = "#a8ff3e"   # lime
GOLD     = "#ffd700"
SOFT_W   = "#e8e8f0"
AREA_CLR = "#1e90ff"


# ══════════════════════════════════════════════
class KinematicEquations(Scene):
# ══════════════════════════════════════════════

    def construct(self):
        self.camera.background_color = BG
        self.intro()
        self.equation1()
        self.equation2()
        self.equation3()
        self.summary()

    # ──────────────────────────────────────────
    def intro(self):
        title = Text("Kinematic Equations", font="Georgia",
                     color=ACCENT1).scale(1.1)
        sub   = Text("for Uniformly Accelerated Motion",
                     font="Georgia", color=SOFT_W).scale(0.55)
        sub.next_to(title, DOWN, buff=0.3)

        eqs = VGroup(
            MathTex(r"v = v_0 + at",            color=ACCENT1),
            MathTex(r"x = v_0 t + \tfrac{1}{2}at^2", color=ACCENT2),
            MathTex(r"v^2 = v_0^2 + 2ax",       color=ACCENT3),
        ).arrange(DOWN, buff=0.4).scale(0.85)
        eqs.next_to(sub, DOWN, buff=0.55)

        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub, shift=UP*0.2))
        self.play(LaggedStart(*[Write(e) for e in eqs], lag_ratio=0.4))
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, sub, eqs)))

    # ──────────────────────────────────────────
    def equation1(self):
        """v = v₀ + at  — from definition of acceleration"""

        # ── Section header
        header = self._section_header("Equation 1", r"v = v_0 + at", ACCENT1)
        self.play(FadeIn(header, shift=DOWN*0.3))
        self.wait(0.4)

        # ── Derivation steps (left column)
        steps = VGroup(
            MathTex(r"\text{By definition:}",         color=SOFT_W),
            MathTex(r"a = \frac{\Delta v}{\Delta t} = \frac{v - v_0}{t}",
                    color=SOFT_W),
            MathTex(r"\Rightarrow\; at = v - v_0",   color=SOFT_W),
            MathTex(r"\boxed{v = v_0 + at}",
                    color=ACCENT1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).scale(0.72)
        steps.to_edge(LEFT, buff=0.9).shift(DOWN*0.4)

        for s in steps[:-1]:
            self.play(Write(s), run_time=0.8)
            self.wait(0.25)
        self.play(Write(steps[-1]), run_time=0.9)

        # ── v-t graph (right column)
        ax = Axes(
            x_range=[0, 4.5, 1], y_range=[0, 7, 1],
            x_length=4.2, y_length=3.4,
            axis_config={"color": SOFT_W, "stroke_width": 2},
            tips=True,
        )
        ax.to_edge(RIGHT, buff=0.7).shift(DOWN*0.5)

        x_label = ax.get_x_axis_label(MathTex("t", color=SOFT_W).scale(0.7),
                                       direction=RIGHT)
        y_label = ax.get_y_axis_label(MathTex("v", color=SOFT_W).scale(0.7),
                                       direction=UP)

        # v = v0 + at  with v0=1.5, a=1.2
        v0, a = 1.5, 1.2
        line = ax.plot(lambda t: v0 + a*t, x_range=[0, 4], color=ACCENT1,
                       stroke_width=3)

        # dashed lines at t=3
        t_val = 3
        v_val = v0 + a*t_val
        dv = DashedLine(ax.c2p(t_val, 0), ax.c2p(t_val, v_val),
                        color=GOLD, dash_length=0.12)
        dh = DashedLine(ax.c2p(0, v_val), ax.c2p(t_val, v_val),
                        color=GOLD, dash_length=0.12)
        dv0 = DashedLine(ax.c2p(0, v0), ax.c2p(t_val, v0),
                         color=ACCENT2, dash_length=0.12)

        lbl_v  = MathTex("v",  color=GOLD).scale(0.6).next_to(
                     ax.c2p(0, v_val), LEFT, buff=0.1)
        lbl_v0 = MathTex("v_0", color=ACCENT2).scale(0.6).next_to(
                     ax.c2p(0, v0), LEFT, buff=0.1)
        lbl_t  = MathTex("t",  color=GOLD).scale(0.6).next_to(
                     ax.c2p(t_val, 0), DOWN, buff=0.1)

        slope_lbl = MathTex(r"\text{slope} = a", color=ACCENT3).scale(0.55)
        slope_lbl.move_to(ax.c2p(2.5, 4.2))

        graph_grp = VGroup(ax, x_label, y_label, line, dv, dh, dv0,
                           lbl_v, lbl_v0, lbl_t, slope_lbl)

        self.play(Create(ax), Write(x_label), Write(y_label))
        self.play(Create(line), run_time=1.2)
        self.play(Create(dv), Create(dh), Create(dv0),
                  Write(lbl_v), Write(lbl_v0), Write(lbl_t))
        self.play(Write(slope_lbl))
        self.wait(2)
        self.play(FadeOut(VGroup(header, steps, graph_grp)))

    # ──────────────────────────────────────────
    def equation2(self):
        """x = v₀t + ½at²  — from area under v-t graph"""

        header = self._section_header("Equation 2",
                                      r"x = v_0 t + \tfrac{1}{2}at^2", ACCENT2)
        self.play(FadeIn(header, shift=DOWN*0.3))
        self.wait(0.4)

        # Derivation steps
        steps = VGroup(
            MathTex(r"\text{Area under } v\text{-}t \text{ graph} = \text{displacement}",
                    color=SOFT_W),
            MathTex(r"x = \text{Area of } \triangle ABC + \text{Area of rect } OACD",
                    color=SOFT_W),
            MathTex(r"x = \tfrac{1}{2}(v-v_0)\,t \;+\; v_0\,t",
                    color=SOFT_W),
            MathTex(r"\text{Since } v - v_0 = at:",
                    color=SOFT_W),
            MathTex(r"\boxed{x = v_0 t + \tfrac{1}{2}at^2}",
                    color=ACCENT2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.65)
        steps.to_edge(LEFT, buff=0.7).shift(DOWN*0.5)

        for s in steps[:-1]:
            self.play(Write(s), run_time=0.75)
            self.wait(0.2)
        self.play(Write(steps[-1]))

        # ── v-t graph with shaded areas
        ax = Axes(
            x_range=[0, 5, 1], y_range=[0, 7, 1],
            x_length=4.2, y_length=3.5,
            axis_config={"color": SOFT_W, "stroke_width": 2},
            tips=True,
        )
        ax.to_edge(RIGHT, buff=0.7).shift(DOWN*0.5)

        x_label = ax.get_x_axis_label(MathTex("t", color=SOFT_W).scale(0.7))
        y_label = ax.get_y_axis_label(MathTex("v", color=SOFT_W).scale(0.7))

        v0, a = 1.5, 1.0
        t_end = 4.0
        v_end = v0 + a*t_end

        line = ax.plot(lambda t: v0 + a*t, x_range=[0, t_end],
                       color=ACCENT2, stroke_width=3)

        # Rectangle (OACD) — v0 * t
        rect_pts = [
            ax.c2p(0, 0),
            ax.c2p(t_end, 0),
            ax.c2p(t_end, v0),
            ax.c2p(0, v0),
        ]
        rect = Polygon(*rect_pts, fill_color=ACCENT2,
                       fill_opacity=0.35, stroke_width=0)

        # Triangle (ABC) — ½(v-v0)*t
        tri_pts = [
            ax.c2p(0, v0),
            ax.c2p(t_end, v0),
            ax.c2p(t_end, v_end),
        ]
        tri = Polygon(*tri_pts, fill_color=AREA_CLR,
                      fill_opacity=0.55, stroke_width=0)

        lbl_rect = MathTex(r"v_0 t", color=ACCENT2).scale(0.55)
        lbl_rect.move_to(ax.c2p(2, v0/2))
        lbl_tri  = MathTex(r"\tfrac{1}{2}at^2", color=ACCENT1).scale(0.55)
        lbl_tri.move_to(ax.c2p(2.8, v0 + 0.9))

        # Corner labels A, B, C, D, O
        def corner(pos, txt, clr=SOFT_W):
            return Text(txt, color=clr).scale(0.45).next_to(pos, DL, buff=0.05)

        lbl_A = Text("A", color=SOFT_W).scale(0.4).next_to(ax.c2p(0, v0),   LEFT,  0.07)
        lbl_B = Text("B", color=SOFT_W).scale(0.4).next_to(ax.c2p(t_end, v_end), UR, 0.07)
        lbl_C = Text("C", color=SOFT_W).scale(0.4).next_to(ax.c2p(t_end, v0), RIGHT, 0.07)
        lbl_D = Text("D", color=SOFT_W).scale(0.4).next_to(ax.c2p(t_end, 0), DR,   0.07)

        graph_grp = VGroup(ax, x_label, y_label, rect, tri, line,
                           lbl_rect, lbl_tri, lbl_A, lbl_B, lbl_C, lbl_D)

        self.play(Create(ax), Write(x_label), Write(y_label))
        self.play(FadeIn(rect), run_time=0.8)
        self.play(FadeIn(tri),  run_time=0.8)
        self.play(Create(line), run_time=1.0)
        self.play(Write(lbl_rect), Write(lbl_tri),
                  Write(lbl_A), Write(lbl_B), Write(lbl_C), Write(lbl_D))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, steps, graph_grp)))

    # ──────────────────────────────────────────
    def equation3(self):
        """v² = v₀² + 2ax  — eliminating t from eq 1 & 2"""

        header = self._section_header("Equation 3",
                                      r"v^2 = v_0^2 + 2ax", ACCENT3)
        self.play(FadeIn(header, shift=DOWN*0.3))
        self.wait(0.4)

        steps = VGroup(
            MathTex(r"\text{From Eq 1: } t = \frac{v - v_0}{a}",
                    color=SOFT_W),
            MathTex(r"\text{Substitute into Eq 2:}",
                    color=SOFT_W),
            MathTex(r"x = v_0\!\left(\frac{v-v_0}{a}\right)"
                    r"+ \frac{1}{2}a\!\left(\frac{v-v_0}{a}\right)^{\!2}",
                    color=SOFT_W),
            MathTex(r"2ax = 2v_0(v-v_0) + (v-v_0)^2",
                    color=SOFT_W),
            MathTex(r"2ax = v^2 - v_0^2",
                    color=SOFT_W),
            MathTex(r"\boxed{v^2 = v_0^2 + 2ax}",
                    color=ACCENT3),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).scale(0.65)
        steps.to_edge(LEFT, buff=0.7).shift(DOWN*0.3)

        for s in steps[:-1]:
            self.play(Write(s), run_time=0.75)
            self.wait(0.2)
        self.play(Write(steps[-1]))

        # ── v² vs x parabola graph
        ax = Axes(
            x_range=[0, 5, 1], y_range=[0, 30, 5],
            x_length=4.0, y_length=3.5,
            axis_config={"color": SOFT_W, "stroke_width": 2},
            tips=True,
        )
        ax.to_edge(RIGHT, buff=0.7).shift(DOWN*0.5)

        x_label = ax.get_x_axis_label(MathTex("x", color=SOFT_W).scale(0.7))
        y_label = ax.get_y_axis_label(MathTex("v^2", color=SOFT_W).scale(0.7))

        v0, a = 2.0, 2.5
        # v² = v0² + 2ax  →  y = v0² + 2a·x
        curve = ax.plot(lambda x: v0**2 + 2*a*x, x_range=[0, 4.8],
                        color=ACCENT3, stroke_width=3)

        # Highlight slope = 2a
        x1, x2 = 1.5, 3.5
        y1 = v0**2 + 2*a*x1
        y2 = v0**2 + 2*a*x2
        slope_line = DashedLine(ax.c2p(x1, y1), ax.c2p(x2, y2),
                                color=GOLD, dash_length=0.12)
        slope_lbl = MathTex(r"\text{slope} = 2a", color=GOLD).scale(0.55)
        slope_lbl.next_to(slope_line, UR, buff=0.1)

        # y-intercept label v0²
        dot_int = Dot(ax.c2p(0, v0**2), color=ACCENT2, radius=0.07)
        lbl_int = MathTex(r"v_0^2", color=ACCENT2).scale(0.6)
        lbl_int.next_to(dot_int, LEFT, buff=0.1)

        graph_grp = VGroup(ax, x_label, y_label, curve,
                           slope_line, slope_lbl, dot_int, lbl_int)

        self.play(Create(ax), Write(x_label), Write(y_label))
        self.play(Create(curve), run_time=1.4)
        self.play(Create(slope_line), Write(slope_lbl))
        self.play(FadeIn(dot_int), Write(lbl_int))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, steps, graph_grp)))

    # ──────────────────────────────────────────
    def summary(self):
        title = Text("Summary", font="Georgia", color=GOLD).scale(0.95)
        title.to_edge(UP, buff=0.5)

        eqs = VGroup(
            VGroup(
                Text("Eq 1", color=ACCENT1).scale(0.5),
                MathTex(r"v = v_0 + at", color=ACCENT1).scale(0.85),
                Text("(velocity–time)", color=SOFT_W).scale(0.42),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Eq 2", color=ACCENT2).scale(0.5),
                MathTex(r"x = v_0 t + \tfrac{1}{2}at^2", color=ACCENT2).scale(0.85),
                Text("(displacement)", color=SOFT_W).scale(0.42),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Eq 3", color=ACCENT3).scale(0.5),
                MathTex(r"v^2 = v_0^2 + 2ax", color=ACCENT3).scale(0.85),
                Text("(velocity–displacement)", color=SOFT_W).scale(0.42),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.5)
        eqs.next_to(title, DOWN, buff=0.5)

        note = Text(
            "These 5 quantities — v₀, v, a, t, x — are connected\n"
            "by these three kinematic equations.",
            color=SOFT_W, font_size=22, line_spacing=1.4,
        )
        note.next_to(eqs, DOWN, buff=0.55)

        self.play(Write(title))
        self.play(LaggedStart(*[FadeIn(e, shift=RIGHT*0.4) for e in eqs],
                               lag_ratio=0.35))
        self.play(FadeIn(note, shift=UP*0.2))
        self.wait(3)

        # Final fade-out flourish
        self.play(FadeOut(VGroup(title, eqs, note)))
        end = Text("Motion in a Straight Line", font="Georgia",
                   color=ACCENT1).scale(0.9)
        ncert = Text("NCERT Physics — Chapter 2", color=SOFT_W).scale(0.5)
        ncert.next_to(end, DOWN, buff=0.25)
        self.play(FadeIn(end), FadeIn(ncert))
        self.wait(2)

    # ──────────────────────────────────────────
    def _section_header(self, label: str, eq_str: str, clr: ManimColor):
        badge = Text(label, color=BG, font_size=22,
                     weight=BOLD)
        badge_bg = SurroundingRectangle(badge, color=clr,
                                        fill_color=clr, fill_opacity=1,
                                        corner_radius=0.15, buff=0.12)
        badge_grp = VGroup(badge_bg, badge)

        eq = MathTex(eq_str, color=clr).scale(0.88)
        eq.next_to(badge_grp, RIGHT, buff=0.35)

        grp = VGroup(badge_grp, eq)
        grp.to_edge(UP, buff=0.35).to_edge(LEFT, buff=0.7)
        return grp