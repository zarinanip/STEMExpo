# STEM Expo
# Name: Zarina Nip
# Visual Studio Code

from manim import *

class SetNotation(Scene):

    # Sets up a method to return a text string with the required spacing, size, font, and highlights
    def defaultFont(self, temp):
            new_text = Text( 
                temp, 
                line_spacing=0.75, 
                font_size=22, 
                font='Arial',
                t2c={" A": RED_C," B": BLUE_D, " G": GREEN},
                t2w={' A': BOLD, ' B': BOLD, ' C': BOLD, ' G': BOLD}
            )
            return new_text

    def construct(self):
        
        ## DEFINING MOBJECTS
        # Define introductory title
        introTitle = Text(
            "Introduction to Set Theory Notation",
            color=WHITE,
            font_size=50,
            font='Times New Roman'
        )
        introName = Text(
             "by Zarina Nip",
             color=WHITE,
             font_size=40,
             font='Times New Roman'
        ).next_to(introTitle, DOWN)

        # Define title banner for graph
        graphTitle = Title("Set Theory Notation").set_y(3.2)

        # Defines the various visual guides (circles/rectangle) and their labels
        circle1 = Circle(radius=2, color=RED_C).set_fill(color=RED_C, opacity=0.55).move_to(4.5*LEFT)
        circle2 = Circle(radius=2, color=BLUE_D).set_fill(color=BLUE_D, opacity=0.45).move_to(2.25*LEFT)
        circle3 = Circle(radius=2, color=GREEN).set_fill(color=GREEN, opacity=0.8)
        rectangle1 = Rectangle(color=WHITE, height=5, width=7.25).next_to(circle1, buff=-4.5)

        vennIntersection = Intersection(circle1, circle2, color=YELLOW).set_opacity(1)
        vennUnion = Union(circle1, circle2, color=PURPLE).set_opacity(1)
        vennExclusionA = Exclusion(rectangle1, circle1, color=LIGHT_GREY).set_opacity(1)
        vennExclusionB = Exclusion(rectangle1, circle2, color=LIGHT_GREY).set_opacity(1)
        vennExclusionAandB = Exclusion(rectangle1, vennUnion, color=LIGHT_BROWN).set_opacity(1)

        labelA = Text("A", color=RED_C, font_size=30, font='Times New Roman')
        labelA.next_to(circle1, direction=LEFT, buff=-0.25).shift(2*UP)
        labelB = Text("B", color=BLUE_D, font_size=30, font='Times New Roman')
        labelB.next_to(circle2, direction=RIGHT, buff=-0.25).shift(2*UP)
        labelC = Text("C", color=WHITE, font_size=30, font='Times New Roman')
        labelC.next_to(rectangle1, direction=RIGHT, buff=0.25).shift(2*DOWN)
        labelG = Text("G", color=GREEN, font_size=30, font='Times New Roman')
        labelG.next_to(circle1, direction=RIGHT, buff=0.23).shift(2*UP)

        # Defines the explanation texts to appear on the right (subsets)
        subsetText1 = self.defaultFont("Let's call the red circle set A.")
        subsetText1.next_to(circle1, buff=1)
        subsetText2 = self.defaultFont(
            "This green circle encompasses the values in A,\n"+
            "containing nothing outside of A."
        ).next_to(circle1, buff=1)
        subsetText3 = self.defaultFont(
            "Let's call the green circle G. When G is\n"+
            "non-zero, and every element is also a part\n"+
            "of A, it is defined as a SUBSET of A."
        ).next_to(circle1, buff=1)
        subsetText4 = self.defaultFont("A subset is notated as ").next_to(circle1, buff=1).shift(0.5*UP)
        subsetFormula1 = MathTex('\subseteq').next_to(subsetText4)
        subsetText5 = self.defaultFont("so this diagram would be").next_to(subsetFormula1)
        subsetText6 = self.defaultFont("described as: ").next_to(subsetText4, 1.5*DOWN, aligned_edge=LEFT)
        subsetFormula2 = MathTex('G \subseteq A').next_to(subsetText6)

        # Defines the explanation texts to appear on the right (proper subsets)
        pSubsetText1 = self.defaultFont(
            "If G is a subset of A and does not equal A, this\n"+
            "would be defined as a PROPER SUBSET."
        ).next_to(circle1, buff=1)
        pSubsetText2 = self.defaultFont("A proper subset is notated as").next_to(circle1, buff=1).shift(0.5*UP)
        pSubsetFormula1 = MathTex('\subset').next_to(pSubsetText2)
        pSubsetText3 = self.defaultFont("so this diagram would be").next_to(pSubsetFormula1)
        pSubsetText4 = self.defaultFont("described as:").next_to(pSubsetText2, 1.5*DOWN, aligned_edge=LEFT)
        pSubsetFormula2 = MathTex('G \subset A').next_to(pSubsetText4)

        # Defines the explanation texts to appear on the right (intersections)
        intersectText1 = self.defaultFont(
            "Here are sets A (in red) and B (in blue)\n"+
            "within a larger set C (the rectangle).\n\n"+
            "Let's say C is a set that contains all\n"+
            "possible elements."
        ).next_to(rectangle1, RIGHT, buff=1)
        intersectText2 = self.defaultFont(
            "Sets A and B overlap in the middle. This\n"+
            "area (highlighted in yellow) is the\n"+
            "INTERSECTION between the two sets.\n"+
            "It contains only elements that are in\n"+
            "sets A and B, excluding the elements\n"+
            "that are only red or only blue."
        ).next_to(rectangle1, buff=1)
        intersectText3 = self.defaultFont("An intersection between two sets is").next_to(rectangle1, buff=1).shift(1.2*UP)
        intersectText4 = self.defaultFont("notated as").next_to(intersectText3, 1.5*DOWN, aligned_edge=LEFT)
        intersectFormula1 = MathTex('\cap').next_to(intersectText4)
        intersectText5 = self.defaultFont("so the intersection").next_to(intersectFormula1)
        intersectText6 = self.defaultFont("between A and B would be described as:").next_to(intersectText4, 1.5*DOWN, aligned_edge=LEFT)
        intersectFormula2 = MathTex('A \cap B').next_to(intersectText3, 6*DOWN, aligned_edge=LEFT)

        # Defines the explanation texts to appear on the right (unions)
        unionText1 = self.defaultFont(
            "The set of elements that are a part of A\n"+
            "or B or both is the UNION between A and B."
        ).next_to(rectangle1, buff=1)
        unionText2 = self.defaultFont("A union is notated as").next_to(rectangle1, RIGHT, buff=1).shift(0.5*UP)
        unionFormula1 = MathTex("\cup").next_to(unionText2)
        unionText3 = self.defaultFont("so this").next_to(unionFormula1)
        unionText4 = self.defaultFont("set is described as:").next_to(unionText2, 1.5*DOWN, aligned_edge=LEFT)
        unionFormula2 = MathTex("A \cup B").next_to(unionText4)

        # Defines the explanation texts to appear on the right (complements)
        compText1 = self.defaultFont(
            "Now that we know how to define elements in\n"+
            "a set/sets, how about elements not in a set?\n"+
            "The area highlighted in grey represents\n"+
            "everything not in set A, defined as the\n"+
            "COMPLEMENT of A."
        ).next_to(rectangle1, buff=1)
        compText2 = self.defaultFont(
            "The complement of A is notated as: "
        ).next_to(rectangle1, buff=1)
        compFormula1 = MathTex("\overline{A}").next_to(compText2)
        compText3 = self.defaultFont(
            "Similarly, the complement of B is "
        ).next_to(rectangle1, buff=1)
        compText4 = self.defaultFont("notated as: ").next_to(compText3, 1.5*DOWN, aligned_edge=LEFT)
        compFormula2 = MathTex("\overline{B}").next_to(compText4)

        # Defines the explanation texts to appear on the right (example)
        exampleText1 = self.defaultFont(
             "Let's put this all together!\n"+
             "What elements are in the set\n"+
             "defined below?"
        ).next_to(rectangle1, buff=1).shift(1*UP)
        exampleFormula1 = MathTex("\overline{A \cup B}").next_to(exampleText1, 1.25*DOWN)
        exampleText2 = self.defaultFont(
             "The answer is highlighted in\n"+
             "gold.Did you get it right?"
        ).next_to(rectangle1, buff=1)

        # Credits
        endingCredits = Paragraph(
            'Credit to:',
            '-',
            'CS 205, taught by Professor Igor Baryakhtar',
            'Discrete Mathematics: An Open Introduction, 3rd edition, written by Oscar Levin',
            '',
            '',
            'Thank you for your help!',
            alignment='center',
            color=WHITE,
            font_size=30,
            font='Times New Roman'
        )

        ## ANIMATING MOBJECTS
        # Animate intro screen
        self.play(Write(introTitle), Write(introName))
        self.play(Wait(3))
        self.play(Unwrite(introTitle,reverse=False), Unwrite(introName, reverse=False))

        # Animating subset explanation
        self.play(FadeIn(graphTitle), Create(circle1))
        self.play(Write(subsetText1), Write(labelA))
        self.pause(2)
        self.play(FadeOut(subsetText1), Create(circle3))
        self.play(circle3.animate.shift(circle1.get_center()), Write(subsetText2))
        self.pause(2)
        self.play(FadeOut(subsetText2))
        self.play(Write(subsetText3), Create(labelG))
        self.pause(3)
        self.play(FadeOut(subsetText3))
        self.play(Write(subsetText4))
        self.play(Write(subsetFormula1))
        self.play(Write(subsetText5))
        self.play(Write(subsetText6))
        self.play(Create(subsetFormula2))
        self.pause(3)
        self.play(
            FadeOut(subsetText4, subsetFormula1, subsetText5, subsetText6, subsetFormula2),
            ScaleInPlace(circle3, scale_factor=0.5)
        )
        self.play(circle3.animate.shift(LEFT))
        self.pause(2)

        # Animating proper subset explanation
        self.play(Write(pSubsetText1))
        self.pause(2)
        self.play(FadeOut(pSubsetText1))
        self.play(Write(pSubsetText2))
        self.play(Write(pSubsetFormula1))
        self.play(Write(pSubsetText3))
        self.play(Write(pSubsetText4))
        self.play(Create(pSubsetFormula2))
        self.pause(3)
        self.play(FadeOut(pSubsetText2, pSubsetFormula1, pSubsetText3, pSubsetText4, pSubsetFormula2, circle3, labelG))

        # Animating intersection explanation
        self.play(Create(circle2), Create(rectangle1))
        self.play(Write(labelB), Write(labelC))
        self.play(Write(intersectText1))
        self.pause(3)
        self.play(FadeOut(intersectText1))
        self.play(DrawBorderThenFill(vennIntersection, run_time=1.5), Write(intersectText2))
        self.pause(3)
        self.play(FadeOut(intersectText2))
        self.play(Write(intersectText3))
        self.play(Write(intersectText4))
        self.play(Create(intersectFormula1))
        self.play(Write(intersectText5))
        self.play(Write(intersectText6))
        self.play(Create(intersectFormula2))
        self.pause(3)
        self.play(FadeOut(vennIntersection, intersectText3, intersectText4, intersectFormula1, intersectText5, intersectText6, intersectFormula2))

        # Animating union explanation
        self.play(Write(unionText1))
        self.play(DrawBorderThenFill(vennUnion, run_time=1.5))
        self.pause(3)
        self.play(FadeOut(unionText1))
        self.play(Write(unionText2))
        self.play(Create(unionFormula1))
        self.play(Write(unionText3))
        self.play(Write(unionText4))
        self.play(Create(unionFormula2))
        self.pause(3)
        self.play(FadeOut(vennUnion, unionText2, unionFormula1, unionText3, unionText4, unionFormula2))

        # Animating complement explanation
        self.play(Create(vennExclusionA), FadeOut(circle2, labelB), Write(compText1))
        self.bring_to_back(vennExclusionA)
        self.pause(3)
        self.play(FadeOut(compText1))
        self.play(Write(compText2))
        self.play(Create(compFormula1))
        self.pause(3)
        self.play(FadeOut(vennExclusionA, compText2, compFormula1), FadeIn(circle2, labelB))
        self.pause(1)
        self.play(Create(vennExclusionB), FadeOut(circle1, labelA))
        self.bring_to_back(vennExclusionB)
        self.play(Write(compText3))
        self.play(Write(compText4))
        self.play(Create(compFormula2))
        self.pause(3)
        self.play(FadeOut(vennExclusionB, compText3, compText4, compFormula2), FadeIn(circle1, labelA))

        # Animating example
        self.play(Write(exampleText1))
        self.play(Create(exampleFormula1))
        self.pause(5)
        self.play(FadeOut(exampleText1, exampleFormula1))
        self.play(Create(vennExclusionAandB))
        self.bring_to_back(vennExclusionAandB)
        self.play(Write(exampleText2))
        self.pause(5)
        self.play(FadeOut(graphTitle, circle1, circle2, rectangle1, labelA, labelB, labelC, vennExclusionAandB, exampleText2))

        # Display ending credits
        self.clear()
        self.play(FadeIn(endingCredits))
        self.pause(2)
        self.play(FadeOut(endingCredits))
        self.clear()

##To run and save the result as a high quality mp4, go into the target folder and run manim -pqh STEMExpo.py SetNotation