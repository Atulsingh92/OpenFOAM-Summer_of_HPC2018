
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
      renderView1.CameraPosition = [0.02761434359065064, -0.03698323033132622, -0.012027898074089206]
      renderView1.CameraFocalPoint = [-0.000369748575189734, 0.0007590860753662898, -0.008207495232733397]
      renderView1.CameraViewUp = [0.043192196653405214, -0.06886343092518996, 0.9966906551330084]
      renderView1.CameraParallelScale = 0.026153393390038217
      renderView1.Background = [1.0, 1.0, 1.0]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='alphaiso_%t.png', freq=4, fittoscreen=0, magnification=1, width=1920, height=1080, cinema={})
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

      # create a new 'Contour'
      contour1 = Contour(Input=viewfoam)
      contour1.ContourBy = ['POINTS', 'alpha.water']
      contour1.ComputeNormals = 0
      contour1.ComputeScalars = 1
      contour1.Isosurfaces = [0.5]
      contour1.PointMergeMethod = 'Uniform Binning'

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------


      # show data from contour1
      contour1Display = Show(contour1, renderView1)

      # get color transfer function/color map for 'alphawater'
      alphawaterLUT = GetColorTransferFunction('alphawater')
      alphawaterLUT.RGBPoints = [0.0, 0.0, 0.0, 1.0, 0.25, 0.0, 1.0, 1.0, 0.5, 0.0, 1.0, 0.0, 0.75, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0]
      alphawaterLUT.ColorSpace = 'RGB'
      alphawaterLUT.ScalarRangeInitialized = 1.0
      alphawaterLUT.AutomaticRescaleRangeMode = 'Grow and update every timestep'

      # trace defaults for the display properties.
      contour1Display.Representation = 'Surface'
      contour1Display.AmbientColor = [0.6666666666666666, 0.0, 0.0]
      contour1Display.ColorArrayName = ['POINTS', 'alpha.water']
      contour1Display.DiffuseColor = [0.0, 0.0, 0.4980392156862745]
      contour1Display.LookupTable = alphawaterLUT
      contour1Display.BackfaceDiffuseColor = [0.0, 0.0, 0.4980392156862745]
      contour1Display.OSPRayScaleArray = 'alpha.water'
      contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
      contour1Display.SelectOrientationVectors = 'None'
      contour1Display.ScaleFactor = 0.00019400004530325534
      contour1Display.SelectScaleArray = 'alpha.water'
      contour1Display.GlyphType = 'Arrow'
      contour1Display.GlyphTableIndexArray = 'alpha.water'
      contour1Display.GaussianRadius = 9.700002265162765e-06
      contour1Display.SetScaleArray = ['POINTS', 'alpha.water']
      contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
      contour1Display.OpacityArray = ['POINTS', 'alpha.water']
      contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
      contour1Display.DataAxesGrid = 'GridAxesRepresentation'
      contour1Display.SelectionCellLabelFontFile = ''
      contour1Display.SelectionPointLabelFontFile = ''
      contour1Display.PolarAxes = 'PolarAxesRepresentation'

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      contour1Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      contour1Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for alphawaterLUT in view renderView1
      alphawaterLUTColorBar = GetScalarBar(alphawaterLUT, renderView1)
      alphawaterLUTColorBar.AutoOrient = 0
      alphawaterLUTColorBar.WindowLocation = 'AnyLocation'
      alphawaterLUTColorBar.Position = [0.7761349693251534, 0.25075528700906347]
      alphawaterLUTColorBar.Title = 'volume fraction'
      alphawaterLUTColorBar.ComponentTitle = ''
      alphawaterLUTColorBar.HorizontalTitle = 1
      alphawaterLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
      alphawaterLUTColorBar.TitleFontFile = ''
      alphawaterLUTColorBar.TitleFontSize = 14
      alphawaterLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
      alphawaterLUTColorBar.LabelFontFile = ''
      alphawaterLUTColorBar.LabelFontSize = 14
      alphawaterLUTColorBar.RangeLabelFormat = '%-#2.1f'
      alphawaterLUTColorBar.TextPosition = 'Ticks left/bottom, annotations right/top'
      alphawaterLUTColorBar.ScalarBarThickness = 14
      alphawaterLUTColorBar.ScalarBarLength = 0.4516614491131763

      # set color bar visibility
      alphawaterLUTColorBar.Visibility = 1

      # show color legend
      contour1Display.SetScalarBarVisibility(renderView1, True)

      annotateTimeFilter1 = AnnotateTimeFilter(Input=viewfoam)
      annotateTimeFilter1.Format = 'Time: %.9f'

      annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1)

      # trace defaults for the display properties.
      annotateTimeFilter1Display.Color = [0.0, 0.0, 0.0]
      annotateTimeFilter1Display.FontFile = ''
      annotateTimeFilter1Display.FontSize = 8
      annotateTimeFilter1Display.WindowLocation = 'LowerCenter'
      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # get opacity transfer function/opacity map for 'alphawater'

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(contour1)
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
