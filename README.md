# jtalkpy
Python rapper module of open_jtalk

## Install

```bash
pip install jtalkpy
```

In order to use this module, `open_jtalk` command must be able to use.
See [OpenJtalk](http://open-jtalk.sourceforge.net/).

#### For Ubuntu system
```bash
sudo apt-get install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001
```
`dict_dir` should be `/var/lib/mecab/dic/open-jtalk/naist-jdic`

`voice_file` should be `/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice`

### For other systems
Pleanse install from [souce](http://open-jtalk.sourceforge.net/).

## VOICE FILES
There are many open source HTS voice model files.

[This page](http://mahoro-ba.net/e1875.html) (Japanse) introduces many models.

## Usage

```python
from jtalkpy import Jtalk
dict_dir = "/var/lib/mecab/dic/open-jtalk/naist-jdic"
voice_file = "/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice"
jtalk = Jtalk(dict_dir, voice_file)
jtalk.from_string("こんにちは、世界", output_file="/home/ubuntu/jtalk_wavs/hello.wav")
```

Open Jtalk options can be set at initialization of `Jtalk` object.
And when `from_string` is called, you can also overwrite these options temporary.


## Contribution
Feel free to create pull request.
1. Fork it ( http://github.com/yhay81/jtalkpy/fork )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)