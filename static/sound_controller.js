function getSoundController() {
    return document.getElementsByClassName('sound-controller')[0];
}


function setSoundVolume() {
    let soundControllerInput = getSoundController();
    fetch('http://192.168.0.104:5000/api/set_sound_volume?sound_volume=' + soundControllerInput.value);
}


let soundControllerInput = getSoundController();
soundControllerInput.addEventListener('change', setSoundVolume);