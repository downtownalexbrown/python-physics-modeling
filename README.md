# python-physics-modeling

Various physics modeling programs which I have built as an independent project for AP Physics class. The best way to see the outputs of programs is to open one of the image files included

sphere.py was largely used to gain familiarity with the matplotlib library. Basic circular motion is employed at an interval of pi/4 radians. The scaling of the axes in the cartesian coordinate system appears to be funky (see the 'circles' that look like ovals), so I opted to move to a polar system.

polar.py is the more complete version of the project. The blue ring represents the elliptical orbit of Earth aroudn the sun. To view some paper calcuations, see work.jpg. The blue dot near the center is the Sun, located on one of the foci. Each value is scaled to million kilometers to keep the values simpler. Seeing as the Earth orbits with an eccentricity of 0.0167, the graph appears circular. 

The final file, orbitpolar.py is an extension of polar.py. By keeping the orbit of the Earth, I can then caculate values of velocity and such to create a moving Earth around the foci. This program is not completed, and still need touching up on. polar.py holds the base for the final step in orbitpolar.py
