def rigid(fixed, moving):
    R = sitk.ImageRegistrationMethod()
    R.SetMetricAsMeanSquares()
    R.SetOptimizerAsRegularStepGradientDescent(8.0, .01, 200 )
    R.SetInitialTransform(sitk.TranslationTransform(sitk.GetImageFromArray(fixed).GetDimension()))
    R.SetInterpolator(sitk.sitkNearestNeighbor)

    R.AddCommand( sitk.sitkIterationEvent, lambda: R )

    outTx = R.Execute(sitk.GetImageFromArray(fixed), sitk.GetImageFromArray(moving))
    
    return outTx

def affine(fixed, moving):
    R = sitk.ImageRegistrationMethod()
    R.SetMetricAsMeanSquares()
#     initial_transform = sitk.CenteredTransformInitializer(sitk.GetImageFromArray(fixed), 
#                                                       sitk.GetImageFromArray(moving), 
#                                                       sitk.AffineTransform(sitk.GetImageFromArray(fixed).GetDimension()))
#     R.SetShrinkFactorsPerLevel([3,2,1])
#     R.SetSmoothingSigmasPerLevel([2,1,1])

#     R.SetMetricAsJointHistogramMutualInformation(20)
    R.MetricUseFixedImageGradientFilterOff()

    R.SetOptimizerAsGradientDescent(learningRate=0.5,
                                    numberOfIterations=200,
                                    estimateLearningRate = R.EachIteration)
    R.SetOptimizerScalesFromPhysicalShift()

    R.SetInitialTransform(sitk.AffineTransform(sitk.GetImageFromArray(fixed).GetDimension()))

    R.SetInterpolator(sitk.sitkLinear)
#     R.SetInitialTransform(sitk.AffineTransform(sitk.GetImageFromArray(fixed).GetDimension()))
#     R.SetInterpolator(sitk.sitkNearestNeighbor)

    R.AddCommand( sitk.sitkIterationEvent, lambda:R )

    outTx = R.Execute(sitk.GetImageFromArray(fixed), sitk.GetImageFromArray(moving))
    
    return outTx

def resample(fixed, moving, outTx, interpolator = sitk.sitkLinear):
#   outTx = sitk.ReadTransform('out.txt')
    resampler = sitk.ResampleImageFilter()
    resampler.SetReferenceImage(sitk.GetImageFromArray(fixed));
    resampler.SetInterpolator(interpolator)
    resampler.SetDefaultPixelValue(0)
    resampler.SetTransform(outTx)
    out = resampler.Execute(sitk.GetImageFromArray(moving))
    
    return out
