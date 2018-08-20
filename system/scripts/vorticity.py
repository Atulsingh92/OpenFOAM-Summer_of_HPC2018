
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
      renderView1.CameraPosition = [0.028862671501890536, -0.04982748264806616, -0.0028916280356488084]
      renderView1.CameraFocalPoint = [0.0012143685754940695, -0.0001238104080324189, -0.007206810022516561]
      renderView1.CameraViewUp = [-0.04600588253187769, 0.06097318147528607, 0.9970785976608088]
      renderView1.CameraParallelScale = 0.026153393390038217
      renderView1.Background = [1.0, 1.0, 1.0]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='vorticity_%t.png', freq=4, fittoscreen=0, magnification=1, width=1920, height=1080, cinema={})
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
      gradientOfUnstructuredDataSet1.ComputeVorticity = 1

      # create a new 'Clip'
      clip1 = Clip(Input=gradientOfUnstructuredDataSet1)
      clip1.ClipType = 'Plane'
      clip1.Scalars = ['POINTS', '']
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

      # get color transfer function/color map for 'Vorticity'
      vorticityLUT = GetColorTransferFunction('Vorticity')      
      vorticityLUT.AutomaticRescaleRangeMode = 'Grow and update every timestep'
      vorticityLUT.RescaleOnVisibilityChange = 1
      vorticityLUT.RGBPoints = [-0.123143121212, 0.0, 0.0, 1.0, 0.8214119492055725, 0.0, 1.0, 1.0, 1.642823898411145, 0.0, 1.0, 0.0, 2.4642358476167177, 1.0, 1.0, 0.0, 30.28564779682229, 1.0, 0.0, 0.0]
      vorticityLUT.ColorSpace = 'RGB'
      vorticityLUT.ScalarRangeInitialized = 1.0
      

      # get opacity transfer function/opacity map for 'Vorticity'
      # trace defaults for the display properties.
      clip1Display.Representation = 'Surface'
      clip1Display.AmbientColor = [0.6666666666666666, 0.0, 0.0]
      clip1Display.ColorArrayName = ['POINTS', 'Vorticity']
      clip1Display.DiffuseColor = [0.0, 0.0, 0.4980392156862745]
      clip1Display.LookupTable = vorticityLUT

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1)

      # trace defaults for the display properties.
      annotateTimeFilter1Display.Color = [0.0, 0.0, 0.0]
      annotateTimeFilter1Display.FontFile = ''
      annotateTimeFilter1Display.FontSize = 8
      annotateTimeFilter1Display.WindowLocation = 'LowerCenter'
      # setup the color legend parameters for each legend in this view

      # get color legend/bar for vorticityLUT in view renderView1
      vorticityLUTColorBar = GetScalarBar(vorticityLUT, renderView1)
      vorticityLUTColorBar.AutoOrient = 0
      vorticityLUTColorBar.WindowLocation = 'AnyLocation'
      vorticityLUTColorBar.Position = [0.7900372455776954, 0.22038460774380675]
      vorticityLUTColorBar.Title = 'Vorticity'
      vorticityLUTColorBar.ComponentTitle = ''
      vorticityLUTColorBar.HorizontalTitle = 1
      vorticityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
      vorticityLUTColorBar.TitleFontFile = ''
      vorticityLUTColorBar.TitleFontSize = 14
      vorticityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
      vorticityLUTColorBar.LabelFontFile = ''
      vorticityLUTColorBar.LabelFontSize = 14
      vorticityLUTColorBar.RangeLabelFormat = '%-#2.1f'
      vorticityLUTColorBar.TextPosition = 'Ticks left/bottom, annotations right/top'
      vorticityLUTColorBar.ScalarBarThickness = 14
      vorticityLUTColorBar.ScalarBarLength = 0.4516614491131766

      # set color bar visibility
      vorticityLUTColorBar.Visibility = 1

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
