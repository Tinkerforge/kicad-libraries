*kicad StepUp 3D mechanical exporter* for collaborative exchange between KiCad and FreeCAD/MCAD;
With *kicad StepUp*, it is possible to work in kicad EDA with the same component model data
available in the *STEP AP214 3D format*, and obtain a 3D STEP AP214 model of the pcb board and
a complete board assemblies with electronic modules, to be used for *MCAD interchange*.
The accurate 3D visualization of components on board assemblies in kicad 3dviewer, is
maintained in the same accuracy and aspect in STEP AP214 format. +
The *kicad StepUp* maintains the usual way to work with kicad, but improves the process
to work in a collaborative way with mechanical designers bringing near ECAD and MCAD environments. +
v4.0.2.9 Mar/2017

please refer to:
kicadStepUp-starter-Guide.pdf
For using in the Tinkerforge environment please refer to howto.txt (work in progress)


*Copyright*
-----------
This document and kicad StepUp scripts are Copyright © 2015 by Maurice.
You may distribute it and/or modify it under the terms of either
the GNU Affero General Public License as published by the Free Software Foundation
to ensure cooperation with the community in the case of network server software;             *
for detail see the LICENCE text file.
http://www.gnu.org/licenses/agpl-3.0.en.html
Moreover you have to include the original author copyright.
All trademarks within this guide belong to their legitimate owners.
Kicad STEPUP (TM) is a TradeMark and cannot be freely useable

Risk disclaimer
---------------
*USE 3D CAD DATA AT YOUR OWN RISK *
*DO NOT RELY UPON ANY INFORMATION FOUND HERE WITHOUT INDEPENDENT VERIFICATION.*


Changelog
---------
- added messages on missing emn files
- added messages on missing models
- added path to adapt your KISYS3DMOD
- added blacklist for unwanted modules
- added messages on blacklisted modules
- added pcb color attribute
- added bounding box option
- added bounding box white list to leave real model on connector or peripheral models
- added auxorigin, base origin, base point placement option
- added vrml models z-rotation angle
- added virtual models option
- added fusion export option
- added saving in native format, export to STEP
- added arcs and circles for calculate board position
- added idf_to_origin flag for version >6091
- added reset properties for FC 016 bug
- added ${KIPRJMOD} support
- added multi 3D vrml model support
- added compatibility to kicad version >=3
- added auto color assigning in bboxes
- added minimum volume per model
- added minimum height per model
- updated findPcbCenter method
- added support for .stp extension beside .step
- added support for .igs extension beside .step
- added support for .iges extension beside .step
- moved all to kicad StepUp tools GUI
- added Load Board from kicad StepUp tools GUI
- added Load Board IDF from kicad StepUp tools GUI
- added kicad StepUp FreeCAD WorkBench to open directly .kicad_pcb, .emn, .kicad_mod files
- added VRML exporter for material properties
- added warning messages
- pad & holes as circles when loading a footprint
- improved multipart load checking
- removed illegal characters in filenames when exporting VRML and STEP
- implemented caching for 3D models
- optimized for fusion w/ colors
- added support for alias i.e. :Kicad3D: as for environment variables
- added crease angle for wrl export 
- added support for ${KISYS3DMOD}/ in new 3d viewer path resolver
- accepting .wrl .step .stp .iges .igs as 3d models directly in kicad_pcb
- added fixedPosition for aligning part to footprint in assembly2
- message if scale values are not assigned to 1 1 1
- added support for wrl offset in position & rotation when loadboard
- added bbox creation based on scaled values (1mm as base unit)
- added height and volume blacklist for scaled shapes
- added error message in case of scale factor not 1:1 for non scaled box
- fixed base point for lower case settings
- added single instance
- added open file type 'rb' 'ab' and write file 'wb' type binary for utf8 full support
- added fix to rect pads in footprint loader
- non blocking warning only for scale <> 1
- fixed minor issues in FC015 loading fp
- fixed utf-8 replace
- fixed minor issues in FC015 loading fp
- added models3Dprefix as default saving location
- added $HOME support for unix systems (it doesn't resolve on win)
- added OCC >=7 FC 0.17 compatibility for Footprint pads, lines, arcs
- added check if the models3Dprefix is writable, otherwise will write on $HOME
- added 2nd path to resolver prefix3d_2
- added wrl materials dialog theme compatibility
- reduced export file size
- accept the new Part.LineSegment using yorik help function FC 0.17 >= 9123
- EdgeCuts for footprint will generate a path on FP loader
- EdgeCuts in footprint will generate Cuts in Board
- accepted utf8 for model in kysys3mod or alias
- checked spaces in name
- added edge tolerance on vertex coincidence
- fixed edge tolerance on FC 017 >9255
- message when adjusting edges
- animation when assembled
- moved config read-write to my own method for full utf-8 support
- accept utf8 on 3D prefix path
- accept utf8 on saving loading last path
- tidy up a bit the utf-8 code
- regenerate ksu-config if too short
- enabled upper case on config
- added message on edge not coincident
- added turntable section
- allowed STEP multipart (creating compound)
- added exception on import step model
- added better theme integration
- improved tolerance on edges
- updated import IDF mod
- added font size in config
- added new way to load step files as compound from vejmarie
- accepted lower and upper case for extension (linux is case sensitive os)
- added align_vrml_step_colors when saving with material properties
- assigned shininess and specular color for single color Shapes
- fixed position for rotated fp-modules with offset
- fixed position for all rotation and offset
- fixed edge cuts for bottom modules
- fixed circle in circle edges
- added tolerance warning > 1e-6 #(1nm) base is mm
- substituted  (== None) -> (is None)
- disabling VBO during loading modules to avoid crashing (new bug from 0.17 after 10101)
- disabling Part-o-Magic observer if exists (not possible without calling the PoM function)
- added full unicode support for names in compounds
- removed activateWorkbench("PartWorkbench") if Assembly2 is active
- added Glass materials to exporting
- added virtual parts skipped message
- most clean code and comments done

- added IDF Importer v3.9.3 FreeCAD WorkBench to correctly import kicad IDF board and parts
  to install the IDFImporter follow these instructions
  http://www.freecadweb.org/wiki/index.php?title=Installing_more_workbenches
  
- added kicadpcb2dxf python utility to export pcbnew drawing layers to dxf 
  **dxf exporter for mechanical layers of a kicad_pcb board**
  - "Dwgs", "Cmts", "Edge", "Eco1", "Eco2", "F.Fab", "B.Fab", "F.CrtYd", "B.CrtYd"
  - the dxf generated has single line draw as it should be for mechanical interchange (this option is missing in pcbnew plot)
  
  how to launch:
  
  **python kicadpcb2dxf.py -f kicad-board.kicad_pcb**
