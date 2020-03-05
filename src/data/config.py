frequencies = [10, 12, 15]
names = ['phone', 'lamp', 'radio']
eeg_stream_name = 'BASIL_Stream'
marker_stream_name = 'psychopy_stimuli'
collector_timeout = 25

weights_classifier = dict()
weights_classifier['spectral'] = 0
weights_classifier['spectral_diff'] = 0.5
weights_classifier['cca'] = 0.5

# for spectral diff method:
# default:
# fq_interval = 0.3
# fq_baseline = 1

fq_interval = 0.3
fq_baseline = 1
