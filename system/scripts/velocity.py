
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
      renderView1.CenterOfRotation = [0.0, 1.2037062152420224e-35, 0.0020000003278255463]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [0.0005149125802836692, -0.06377338197691258, -0.0068107260459172305]
      renderView1.CameraFocalPoint = [0.0005149125802836692, 1.2037062152420224e-35, -0.0068107260459172305]
      renderView1.CameraViewUp = [0.0, 0.0, 1.0]
      renderView1.CameraParallelScale = 0.02416609174617284
      renderView1.Background = [1.0, 1.0, 1.0]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='velocity_%t.png', freq=4, fittoscreen=0, magnification=1, width=1920, height=1080, cinema={})
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

      # create a new 'Slice'
      slice1 = Slice(Input=viewfoam)
      slice1.SliceType = 'Plane'
      slice1.SliceOffsetValues = [0.0]

      # init the 'Plane' selected for 'SliceType'
      slice1.SliceType.Origin = [0.0, 0.0, 0.0020000003278255463]
      slice1.SliceType.Normal = [0.0, 1.0, 0.0]

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------
      annotateTimeFilter1 = AnnotateTimeFilter(Input=viewfoam)
      annotateTimeFilter1.Format = 'Time: %.9f'

      # show data from slice1
      slice1Display = Show(slice1, renderView1)

      # get color transfer function/color map for 'U'
      uLUT = GetColorTransferFunction('U')
      uLUT.AutomaticRescaleRangeMode = 'Grow and update every timestep'
      uLUT.RescaleOnVisibilityChange = 1
      uLUT.RGBPoints = [6.32454e-05, 0.0, 0.0, 1.0, 2.75004743405, 0.0, 1.0, 1.0, 5.5000316227, 0.0, 1.0, 0.0, 8.25001581135, 1.0, 1.0, 0.0, 30, 1.0, 0.0, 0.0]
      uLUT.ColorSpace = 'RGB'
      uLUT.ScalarRangeInitialized = 1.0

      # trace defaults for the display properties.
      slice1Display.Representation = 'Surface'
      slice1Display.AmbientColor = [0.6666666666666666, 0.0, 0.0]
      slice1Display.ColorArrayName = ['POINTS', 'U']
      slice1Display.DiffuseColor = [0.0, 0.0, 0.4980392156862745]
      slice1Display.LookupTable = uLUT
      slice1Display.BackfaceDiffuseColor = [0.0, 0.0, 0.4980392156862745]
      slice1Display.OSPRayScaleArray = 'U'
      slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
      slice1Display.SelectOrientationVectors = 'U'
      slice1Display.ScaleFactor = 0.004399999976158142
      slice1Display.SelectScaleArray = 'None'
      slice1Display.GlyphType = 'Arrow'
      slice1Display.GlyphTableIndexArray = 'None'
      slice1Display.GaussianRadius = 0.00021999999880790712
      slice1Display.SetScaleArray = ['POINTS', 'U']
      slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
      slice1Display.OpacityArray = ['POINTS', 'U']
      slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
      slice1Display.DataAxesGrid = 'GridAxesRepresentation'
      slice1Display.SelectionCellLabelFontFile = ''
      slice1Display.SelectionPointLabelFontFile = ''
      slice1Display.PolarAxes = 'PolarAxesRepresentation'

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      slice1Display.ScaleTransferFunction.Points = [-2.4205879526562057e-05, 0.0, 0.5, 0.0, 2.4205863155657426e-05, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      slice1Display.OpacityTransferFunction.Points = [-2.4205879526562057e-05, 0.0, 0.5, 0.0, 2.4205863155657426e-05, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1)

      # trace defaults for the display properties.
      annotateTimeFilter1Display.Color = [0.0, 0.0, 0.0]
      annotateTimeFilter1Display.FontFile = ''
      annotateTimeFilter1Display.FontSize = 8
      annotateTimeFilter1Display.WindowLocation = 'LowerCenter'
      # setup the color legend parameters for each legend in this view

      # get color legend/bar for uLUT in view renderView1
      uLUTColorBar = GetScalarBar(uLUT, renderView1)
      uLUTColorBar.AutoOrient = 0
      uLUTColorBar.WindowLocation = 'AnyLocation'
      uLUTColorBar.Position = [0.7286004514672686, 0.3141176470588236]
      uLUTColorBar.Title = 'U'
      uLUTColorBar.ComponentTitle = '[m/s]'
      uLUTColorBar.HorizontalTitle = 1
      uLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
      uLUTColorBar.TitleFontFile = ''
      uLUTColorBar.TitleFontSize = 14
      uLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
      uLUTColorBar.LabelFontFile = ''
      uLUTColorBar.LabelFontSize = 14
      uLUTColorBar.RangeLabelFormat = '%-#2.1f'
      uLUTColorBar.TextPosition = 'Ticks left/bottom, annotations right/top'
      uLUTColorBar.ScalarBarThickness = 14
      uLUTColorBar.ScalarBarLength = 0.45166144911317585

      # set color bar visibility
      uLUTColorBar.Visibility = 1

      # show color legend
      slice1Display.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # get opacity transfer function/opacity map for 'U'
      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(slice1)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'region': [4, 4]}
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
