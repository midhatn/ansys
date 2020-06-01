# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.1.0
# 12:33:40  Jun 01, 2020
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.InsertDesign("HFSS", "RectInset_ATK", "DrivenModal", "")
oDesign = oProject.SetActiveDesign("RectInset_ATK")
oDesign.SetDesignSettings(
	[
		"NAME:Design Settings Data",
		"Use Advanced DC Extrapolation:=", False,
		"Use Power S:="		, False,
		"Export After Simulation:=", False,
		"Allow Material Override:=", True,
		"Calculate Lossy Dielectrics:=", False,
		"Perform Minimal validation:=", False,
		"EnabledObjects:="	, [],
		"Port Validation Settings:=", "Standard"
	])
oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.AddMaterial(
	[
		"NAME:FR4_epoxy",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Electromagnetic"]
		],
		"permittivity:="	, "4.4",
		"conductivity:="	, "0",
		"dielectric_loss_tangent:=", "0.02"
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.SetModelUnits(
	[
		"NAME:Units Parameter",
		"Units:="		, "cm",
		"Rescale:="		, False
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:--Antenna Dimensions",
					"PropType:="		, "SeparatorProp",
					"UserDef:="		, True,
					"Value:="		, ""
				],
				[
					"NAME:patchX",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "11.86cm"
				],
				[
					"NAME:patchY",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "10.04cm"
				],
				[
					"NAME:--Substrate Dimensions",
					"PropType:="		, "SeparatorProp",
					"UserDef:="		, True,
					"Value:="		, ""
				],
				[
					"NAME:subH",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.1575cm"
				],
				[
					"NAME:subX",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "18.7cm"
				],
				[
					"NAME:subY",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "29.74cm"
				],
				[
					"NAME:--Feed Dimensions",
					"PropType:="		, "SeparatorProp",
					"UserDef:="		, True,
					"Value:="		, ""
				],
				[
					"NAME:InsetDistance",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "3.067cm"
				],
				[
					"NAME:InsetGap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.247cm"
				],
				[
					"NAME:FeedWidth",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.493cm"
				],
				[
					"NAME:FeedLength",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "9.138cm"
				]
			]
		]
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-subX/2",
		"YPosition:="		, "-subY/2",
		"ZPosition:="		, "0cm",
		"XSize:="		, "subX",
		"YSize:="		, "subY",
		"ZSize:="		, "subH"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "NewObject_ALJ23O",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.3,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"NewObject_ALJ23O"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "sub"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"sub"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Material",
					"Value:="		, "\"FR4_epoxy\""
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"sub"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 0,
					"G:="			, 128,
					"B:="			, 0
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-subX/2",
		"YStart:="		, "-subY/2",
		"ZStart:="		, "0cm",
		"Width:="		, "subX",
		"Height:="		, "subY",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "NewObject_SQBC1P",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.3,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"NewObject_SQBC1P"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Ground"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Ground"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 65
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-patchX/2",
		"YStart:="		, "-patchY/2",
		"ZStart:="		, "subH",
		"Width:="		, "patchX",
		"Height:="		, "patchY",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "NewObject_7ICZDJ",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.3,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"NewObject_7ICZDJ"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "antenna"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"antenna"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 65
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-FeedWidth/2-InsetGap",
		"YStart:="		, "patchY/2-InsetDistance",
		"ZStart:="		, "subH",
		"Width:="		, "FeedWidth+2*InsetGap",
		"Height:="		, "FeedLength",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "NewObject_RWD5JL",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.3,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "antenna",
		"Tool Parts:="		, "NewObject_RWD5JL"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-FeedWidth/2",
		"YStart:="		, "patchY/2-InsetDistance",
		"ZStart:="		, "subH",
		"Width:="		, "FeedWidth",
		"Height:="		, "FeedLength+InsetDistance",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "NewObject_G6ISUM",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.3,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "antenna,NewObject_G6ISUM"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-FeedWidth/2",
		"YStart:="		, "patchY/2+FeedLength",
		"ZStart:="		, "0cm",
		"Width:="		, "subH",
		"Height:="		, "FeedWidth",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "NewObject_9GLOWR",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0.3,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"NewObject_9GLOWR"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "port1"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"port1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 128,
					"G:="			, 0,
					"B:="			, 0
				]
			]
		]
	])
oDesign.SetSolutionType("DrivenTerminal", False)
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignPerfectE(
	[
		"NAME:antennaMetal",
		"Objects:="		, ["antenna"],
		"InfGroundPlane:="	, False
	])
oModule.AssignPerfectE(
	[
		"NAME:groundMetal",
		"Objects:="		, ["Ground"],
		"InfGroundPlane:="	, False
	])
oModule = oDesign.GetModule("ModelSetup")
oModule.CreateOpenRegion(
	[
		"NAME:Settings",
		"OpFreq:="		, "1GHz",
		"Boundary:="		, "Radiation",
		"ApplyInfiniteGP:="	, False
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AutoIdentifyPorts(
	[
		"NAME:Faces", 
		105
	], False, 
	[
		"NAME:ReferenceConductors", 
		"antenna"
	], "1", True)
oModule.SetTerminalReferenceImpedances("50ohm", "1", True)
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:ATK_Solution",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "1GHz",
		"MaxDeltaS:="		, 0.02,
		"PortsOnly:="		, False,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 15,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "ACA",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced"
	])
oModule.InsertFrequencySweep("ATK_Solution", 
	[
		"NAME:FF_Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearCount",
		"RangeStart:="		, "0.5GHz",
		"RangeEnd:="		, "1.5GHz",
		"RangeCount:="		, 3,
		"Type:="		, "Discrete",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"ExtrapToDC:="		, False
	])
oModule.InsertFrequencySweep("ATK_Solution", 
	[
		"NAME:SParam_Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearCount",
		"RangeStart:="		, "0.5GHz",
		"RangeEnd:="		, "1.5GHz",
		"RangeCount:="		, 100,
		"Type:="		, "Interpolating",
		"SaveFields:="		, False,
		"SaveRadFields:="	, False,
		"InterpTolerance:="	, 0.5,
		"InterpMaxSolns:="	, 250,
		"InterpMinSolns:="	, 0,
		"InterpMinSubranges:="	, 1,
		"ExtrapToDC:="		, False,
		"InterpUseS:="		, True,
		"InterpUsePortImped:="	, True,
		"InterpUsePropConst:="	, True,
		"UseDerivativeConvergence:=", False,
		"InterpDerivTolerance:=", 0.2,
		"UseFullBasis:="	, True,
		"EnforcePassivity:="	, True,
		"PassivityErrorTolerance:=", 0.0001,
		"EnforceCausality:="	, False
	])
oModule = oDesign.GetModule("RadField")
oModule.InsertFarFieldSphereSetup(
	[
		"NAME:ATK_2D",
		"UseCustomRadiationSurface:=", False,
		"ThetaStart:="		, "-180deg",
		"ThetaStop:="		, "180deg",
		"ThetaStep:="		, "1deg",
		"PhiStart:="		, "0deg",
		"PhiStop:="		, "90deg",
		"PhiStep:="		, "90deg",
		"UseLocalCS:="		, False
	])
oModule.InsertFarFieldSphereSetup(
	[
		"NAME:ATK_3D",
		"UseCustomRadiationSurface:=", False,
		"ThetaStart:="		, "-180deg",
		"ThetaStop:="		, "180deg",
		"ThetaStep:="		, "2deg",
		"PhiStart:="		, "0deg",
		"PhiStop:="		, "180deg",
		"PhiStep:="		, "5deg",
		"UseLocalCS:="		, False
	])
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("ff_3D_GainTotal", "Far Fields", "3D Polar Plot", "ATK_Solution : LastAdaptive", 
	[
		"Context:="		, "ATK_3D"
	], 
	[
		"Phi:="			, ["All"],
		"Theta:="		, ["All"],
		"Freq:="		, ["1000000000"]
	], 
	[
		"Phi Component:="	, "Phi",
		"Theta Component:="	, "Theta",
		"Mag Component:="	, ["dB(GainTotal)"]
	])
oModule.CreateReport("ff_2D_GainTotal", "Far Fields", "Radiation Pattern", "ATK_Solution : LastAdaptive", 
	[
		"Context:="		, "ATK_2D"
	], 
	[
		"Theta:="		, ["All"],
		"Phi:="			, ["All"],
		"Freq:="		, ["1000000000"]
	], 
	[
		"Ang Component:="	, "Theta",
		"Mag Component:="	, ["dB(GainTotal)"]
	])
oModule.CreateReport("ff_2D_GainTotal_Stacked", "Far Fields", "Rectangular Stacked Plot", "ATK_Solution : FF_Sweep", 
	[
		"Context:="		, "ATK_2D"
	], 
	[
		"Theta:="		, ["All"],
		"Phi:="			, ["All"],
		"Freq:="		, ["All"]
	], 
	[
		"X Component:="		, "Theta",
		"Y Component:="		, ["dB(GainTotal)"]
	])
oModule.CreateReport("Return Loss", "Terminal Solution Data", "Rectangular Plot", "ATK_Solution : SParam_Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(St11)"]
	])
oModule.CreateReport("Input Impedance", "Terminal Solution Data", "Smith Chart", "ATK_Solution : SParam_Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"]
	], 
	[
		"Polar Component:="	, ["St11"]
	])
oProject.Save()
oDesign.AnalyzeAllNominal()
