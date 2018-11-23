import subprocess
from typing import Union


class Jtalk:
    def __init__(self,
                 dict_dir,
                 voice_file,
                 output_file='/dev/null',
                 trace_file='/dev/null',
                 sampling='auto',
                 frame_period='auto',
                 all_pass='auto',
                 filter_coefficient=0.0,
                 speed_rate=1.0,
                 half_tone=0.0,
                 threshold=0.5,
                 spectrum=1.0,
                 log_f0=1.0,
                 volume=0.0,
                 buffer=0
                 ):
        """
        in ubuntu apt-get;
            dict_dir = "/var/lib/mecab/dic/open-jtalk/naist-jdic"
            voice_file = "/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice"
        :param dict_dir:           -x  dir      : dictionary directory                              [  N/A]
        :param voice_file:         -m  htsvoice : HTS voice files                                   [  N/A]
        :param output_file:        -ow s        : filename of output wav audio (generated speech)   [  N/A]
        :param trace_file:         -ot s        : filename of output trace information              [  N/A]
        :param sampling:           -s  i        : sampling frequency                                [ auto][   1--    ]
        :param frame_period:       -s  i        : sampling frequency                                [ auto][   1--    ]
        :param all_pass:           -a  f        : all-pass constant                                 [ auto][ 0.0-- 1.0]
        :param filter_coefficient: -b  f        : postfiltering coefficient                         [  0.0][ 0.0-- 1.0]
        :param speed_rate:         -r  f        : speech speed rate                                 [  1.0][ 0.0--    ]
        :param half_tone:          -fm f        : additional half-tone                              [  0.0][    --    ]
        :param threshold:          -u  f        : voiced/unvoiced threshold                         [  0.5][ 0.0-- 1.0]
        :param spectrum:           -jm f        : weight of GV for spectrum                         [  1.0][ 0.0--    ]
        :param log_f0:             -jf f        : weight of GV for log F0                           [  1.0][ 0.0--    ]
        :param volume:             -g  f        : volume (dB)                                       [  0.0][    --    ]
        :param buffer:             -z  i        : audio buffer size (if i==0, turn off)             [    0][   0--    ]
        """
        self._dict_dir = dict_dir
        self._voice_file = voice_file
        self._output_file = output_file
        self._trace_file = trace_file
        self._sampling = sampling
        self._frame_period = frame_period
        self._all_pass = all_pass
        self._filter_coefficient = filter_coefficient
        self._speed_rate = speed_rate
        self._half_tone = half_tone
        self._log_f0 = log_f0
        self._threshold = threshold
        self._spectrum = spectrum
        self._volume = volume
        self._buffer = buffer

    @property
    def dict_dir(self) -> str:
        return self._dict_dir

    @property
    def voice_file(self) -> str:
        return self._voice_file

    @property
    def output_file(self) -> str:
        return self._output_file

    @property
    def trace_file(self) -> str:
        return self._trace_file

    @property
    def sampling(self) -> Union[int, str]:
        return self._sampling

    @property
    def frame_period(self) -> Union[int, str]:
        return self._frame_period

    @property
    def all_pass(self) -> Union[float, str]:
        return self._all_pass

    @property
    def filter_coefficient(self) -> float:
        return self._filter_coefficient

    @property
    def speed_rate(self) -> float:
        return self._speed_rate

    @property
    def half_tone(self) -> float:
        return self._half_tone

    @property
    def log_f0(self) -> float:
        return self._log_f0

    @property
    def spectrum(self) -> float:
        return self._spectrum

    @property
    def volume(self) -> float:
        return self._volume

    @property
    def buffer(self) -> float:
        return self._buffer

    def from_string(self,
                    string,
                    dict_dir=None,
                    voice_file=None,
                    output_file=None,
                    trace_file=None,
                    sampling=None,
                    frame_period=None,
                    all_pass=None,
                    filter_coefficient=None,
                    speed_rate=None,
                    half_tone=None,
                    threshold=None,
                    spectrum=None,
                    log_f0=None,
                    volume=None,
                    buffer=None,
                    timeout=60):
        command = [
            'open_jtalk',
            '-x', dict_dir or self._dict_dir,
            '-m', voice_file or self._voice_file,
            '-ow', trace_file or self._trace_file,
            '-ot', sampling or self._sampling,
            '-s', frame_period or self._frame_period,
            '-p', all_pass or self._all_pass,
            '-a', filter_coefficient or self._filter_coefficient,
            '-b', speed_rate or self._speed_rate,
            '-fm', half_tone or self._half_tone,
            '-u', threshold or self._threshold,
            '-jm', spectrum or self._spectrum,
            '-jf', log_f0 or self._log_f0,
            '-g', volume or self._volume,
            '-z', buffer or self._buffer
        ]
        proc = subprocess.Popen(command, stdin=subprocess.PIPE)
        proc.stdin.write(string)
        proc.stdin.close()
        proc.wait(timeout=timeout)
        return output_file

    def from_file(self,
                  infile,
                  dict_dir=None,
                  voice_file=None,
                  output_file=None,
                  trace_file=None,
                  sampling=None,
                  frame_period=None,
                  all_pass=None,
                  filter_coefficient=None,
                  speed_rate=None,
                  half_tone=None,
                  threshold=None,
                  spectrum=None,
                  log_f0=None,
                  volume=None,
                  buffer=None,
                  timeout=60):
        command = [
            'open_jtalk',
            '-x', dict_dir or self._dict_dir,
            '-m', voice_file or self._voice_file,
            '-ow', trace_file or self._trace_file,
            '-ot', sampling or self._sampling,
            '-s', frame_period or self._frame_period,
            '-p', all_pass or self._all_pass,
            '-a', filter_coefficient or self._filter_coefficient,
            '-b', speed_rate or self._speed_rate,
            '-fm', half_tone or self._half_tone,
            '-u', threshold or self._threshold,
            '-jm', spectrum or self._spectrum,
            '-jf', log_f0 or self._log_f0,
            '-g', volume or self._volume,
            '-z', buffer or self._buffer,
            infile
        ]
        process = subprocess.Popen(command, stdin=subprocess.PIPE)
        process.wait(timeout=timeout)
        return output_file
