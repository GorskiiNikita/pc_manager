import alsaaudio


def get_current_sound_value():
    m = alsaaudio.Mixer()
    return m.getvolume()[0]


def set_sound_volume(vol):
    m = alsaaudio.Mixer()
    m.setvolume(vol)

