
from paraview.simple import *
from paraview import coprocessing


#--------------------------------------------------------------
# Code generated from cpstate.py to create the CoProcessor.
# paraview version 5.5.1

#--------------------------------------------------------------
# Global screenshot output options
imageFileNamePadding=0
rescale_lookuptable=False


# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      # state file generated using paraview version 5.5.1

      # ----------------------------------------------------------------
      # setup views used in the visualization
      # ----------------------------------------------------------------

      # trace generated using paraview version 5.5.1

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [1920,1080]
      renderView1.AnnotationColor = [0.0, 0.0, 0.0]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
      renderView1.OrientationAxesOutlineColor = [0.6666666666666666, 0.0, 0.0]
      renderView1.CenterOfRotation = [0.0, 0.0, 0.0020000003278255463]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [0.028710203368034884, -0.047453125431762055, -0.01435024424380998]
      renderView1.CameraFocalPoint = [0.0011163465105231314, 0.0019544523560694692, -0.007210580014937018]
      renderView1.CameraViewUp = [0.05398625986313298, -0.11321325577279248, 0.9921029394489841]
      renderView1.CameraParallelScale = 0.026153393390038217
      renderView1.Background = [1.0, 1.0, 1.0]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='qcrit_%t.png', freq=4, fittoscreen=0, magnification=1, width=1920, height=1080, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # ----------------------------------------------------------------
      # restore active view
      SetActiveView(renderView1)
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # setup the data processing pipelines
      # ----------------------------------------------------------------

      # create a new 'OpenFOAMReader'
      # create a producer from a simulation input
      viewfoam = coprocessor.CreateProducer(datadescription, 'region')

      # create a new 'Gradient Of Unstructured DataSet'
      gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(Input=viewfoam)
      gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'U']
      gradientOfUnstructuredDataSet1.ComputeGradient = 0
      gradientOfUnstructuredDataSet1.ComputeQCriterion = 1

      # create a new 'Clip'
      clip1 = Clip(Input=gradientOfUnstructuredDataSet1)
      clip1.ClipType = 'Plane'
      clip1.Scalars = ['POINTS', 'Q-criterion']
      clip1.Value = -0.15490560233592987
      clip1.Invert = 0

      # init the 'Plane' selected for 'ClipType'
      clip1.ClipType.Origin = [0.0, 0.0, 0.0020000003278255463]
      clip1.ClipType.Normal = [0.0, 1.0, 0.0]

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------
      annotateTimeFilter1 = AnnotateTimeFilter(Input=viewfoam)
      annotateTimeFilter1.Format = 'Time: %.9f'

      # show data from clip1
      clip1Display = Show(clip1, renderView1)

      # get color transfer function/color map for 'Qcriterion'
      qcriterionLUT = GetColorTransferFunction('Qcriterion')      
      qcriterionLUT.AutomaticRescaleRangeMode = 'Grow and update every timestep'
      qcriterionLUT.RescaleOnVisibilityChange = 1
      qcriterionLUT.RGBPoints = [-3.3, 0.0, 0.0, 1.0, -1.529579609632492, 0.0, 1.0, 1.0, -0.4088537096977234, 0.0, 1.0, 0.0, 0.7118721902370453, 1.0, 1.0, 0.0, 10.32598090171814, 1.0, 0.0, 0.0]
      qcriterionLUT.ColorSpace = 'RGB'
      qcriterionLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'Qcriterion'

      # trace defaults for the display properties.
      clip1Display.Representation = 'Surface'
      clip1Display.AmbientColor = [0.6666666666666666, 0.0, 0.0]
      clip1Display.ColorArrayName = ['POINTS', 'Q-criterion']
      clip1Display.DiffuseColor = [0.0, 0.0, 0.4980392156862745]
      clip1Display.LookupTable = qcriterionLUT

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1)

      # trace defaults for the display properties.
      annotateTimeFilter1Display.Color = [0.0, 0.0, 0.0]
      annotateTimeFilter1Display.FontFile = ''
      annotateTimeFilter1Display.FontSize = 8
      annotateTimeFilter1Display.WindowLocation = 'LowerCenter'
      # setup the color legend parameters for each legend in this view

      # get color legend/bar for qcriterionLUT in view renderView1
      qcriterionLUTColorBar = GetScalarBar(qcriterionLUT, renderView1)
      qcriterionLUTColorBar.AutoOrient = 0
      qcriterionLUTColorBar.WindowLocation = 'AnyLocation'
      qcriterionLUTColorBar.Position = [0.7650617283950618, 0.2045454545454546]
      qcriterionLUTColorBar.Title = 'Q-criterion'
      qcriterionLUTColorBar.ComponentTitle = ''
      qcriterionLUTColorBar.HorizontalTitle = 1
      qcriterionLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
      qcriterionLUTColorBar.TitleFontFile = ''
      qcriterionLUTColorBar.TitleFontSize = 14
      qcriterionLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
      qcriterionLUTColorBar.LabelFontFile = ''
      qcriterionLUTColorBar.LabelFontSize = 14
      qcriterionLUTColorBar.RangeLabelFormat = '%-#2.1f'
      qcriterionLUTColorBar.TextPosition = 'Ticks left/bottom, annotations right/top'
      qcriterionLUTColorBar.ScalarBarThickness = 14
      qcriterionLUTColorBar.ScalarBarLength = 0.4516614491131764

      # set color bar visibility
      qcriterionLUTColorBar.Visibility = 1

      # show color legend
      clip1Display.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(clip1)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'region': [4, 4, 4]}
  coprocessor.SetUpdateFrequencies(freqs)
  return coprocessor


#--------------------------------------------------------------
# Global variable that will hold the pipeline for each timestep
# Creating the CoProcessor object, doesn't actually create the ParaView pipeline.
# It will be automatically setup when coprocessor.UpdateProducers() is called the
# first time.
coprocessor = CreateCoProcessor()

#--------------------------------------------------------------
# Enable Live-Visualizaton with ParaView and the update frequency
coprocessor.EnableLiveVisualization(True, 1)

# ---------------------- Data Selection method ----------------------

def RequestDataDescription(datadescription):
    "Callback to populate the request for current timestep"
    global coprocessor
    if datadescription.GetForceOutput() == True:
        # We are just going to request all fields and meshes from the simulation
        # code/adaptor.
        for i in range(datadescription.GetNumberOfInputDescriptions()):
            datadescription.GetInputDescription(i).AllFieldsOn()
            datadescription.GetInputDescription(i).GenerateMeshOn()
        return

    # setup requests for all inputs based on the requirements of the
    # pipeline.
    coprocessor.LoadRequestedData(datadescription)

# ------------------------ Processing method ------------------------

def DoCoProcessing(datadescription):
    "Callback to do co-processing for current timestep"
    global coprocessor

    # Update the coprocessor by providing it the newly generated simulation data.
    # If the pipeline hasn't been setup yet, this will setup the pipeline.
    coprocessor.UpdateProducers(datadescription)

    # Write output data, if appropriate.
    coprocessor.WriteData(datadescription);

    # Write image capture (Last arg: rescale lookup table), if appropriate.
    coprocessor.WriteImages(datadescription, rescale_lookuptable=rescale_lookuptable,
        image_quality=0, padding_amount=imageFileNamePadding)

    # Live Visualization, if enabled.
    coprocessor.DoLiveVisualization(datadescription, "localhost", 22222)
