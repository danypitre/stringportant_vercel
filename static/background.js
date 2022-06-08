



function copy() { 
    let toCopy = document.getElementById("words-container").innerText
    let copyBtn = document.getElementById("copy-btn")

    navigator.clipboard.writeText(toCopy)
    copyBtn.classList.add("copied")
    copyBtn.innerText = 'Copied ! '
    
}

function loading(){ 

    let loader = document.querySelector('.loading')
    let loaderWarning = document.getElementById("warningLoading")
    let number = document.getElementById("number")
    if (number.value >= 10000){
        loaderWarning.classList.remove("hidden")
    }
    loader.classList.remove("hidden")
    setInterval(threeDots, 500)



    
}

function threeDots(){
    let loader = document.querySelector('#loadingDots')
    console.log(loader.innerText)

    if (loader.innerText == '...') { 
        loader.innerText = '.'
    }
    else if (loader.innerText == '.') { 
        loader.innerText = '..'
    }
    else{
        loader.innerText = '...'
    }



}

