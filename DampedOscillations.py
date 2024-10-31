from manim import *

import numpy as np

class dampedOscillation(Scene):

    def functio(self,x):
        return 8*pow(2.718281,-.12*x)*np.cos(3*x)

    def construct(self):
        plane = Axes(x_range=[0,25,1],y_range=[-10,10,1],x_length=12,y_length=10)
        Tracker = ValueTracker(0)
        self.play(Create(plane))
        self.wait(2)
        e = 2.718281
        dampedOsc = always_redraw(lambda : plane.plot(lambda x: 8*pow(e,-.12*x)*np.cos(3*x),x_range=[0,Tracker.get_value()]))

        dot = always_redraw(lambda : Dot(color=YELLOW,point = plane.coords_to_point(Tracker.get_value(),self.functio(Tracker.get_value()),0)))
 
        amplitudeTracker = always_redraw(lambda : plane.plot(lambda x: 8*pow(e,-.12*x) , x_range=[0,Tracker.get_value()],color=YELLOW))
 
        dot2 = always_redraw(lambda : Dot(color=YELLOW,point = plane.coords_to_point(Tracker.get_value(),8*pow(e,-.12*Tracker.get_value()),0)))
 
        amplitudeTracker1 = always_redraw(lambda : plane.plot(lambda x: -8*pow(e,-.12*x) , x_range=[0,Tracker.get_value()],color=YELLOW))

        dot3 = always_redraw(lambda : Dot(color=YELLOW,point = plane.coords_to_point(Tracker.get_value(),-8*pow(e,-.12*Tracker.get_value()),0)))
 

        equation = MathTex(r"y = e^{-0.12x} \cos(3x)")
        equation.move_to(plane.get_center()+np.array([0,3.4,0]))
        self.play(Write(equation))
        self.add(amplitudeTracker)
        self.add(dot)
        self.add(dot3)
        self.add(amplitudeTracker1)
        self.add(dot2)
        self.add(dampedOsc)
        self.play(Tracker.animate.set_value(24),rate_func=linear,run_time=15)
        self.wait(2)

