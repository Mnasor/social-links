import streamlit as st


def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()),
                    unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


def st_button(icon, url, label, iconsize):
    if icon == 'youtube':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-youtube" viewBox="0 0 16 16">
                    <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
                </svg>  
                {label}
            </a>
        </p>'''
    elif icon == 'snapchat':
        button_code = f'''
        <p>
        <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
            <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-snapchat" viewBox="0 0 22 22">
                <path d= 'M21.79755,16.98718c-2.86621-.47223-4.15094-3.40149-4.204-3.52588l-.00544-.01172a1.07048,1.07048,0,0,1-.10223-.89758c.19251-.45361.82935-.6557,1.25134-.78967.10535-.03339.205-.065.28315-.096.76275-.30127.91784-.61316.91406-.8219a.66226.66226,0,0,0-.50134-.54358l-.00568-.00213a.9462.9462,0,0,0-.35632-.06824.7546.7546,0,0,0-.31287.06207,2.54,2.54,0,0,1-.95526.26612.82134.82134,0,0,1-.52954-.17725c.00915-.16992.02-.34522.0318-.53046l.004-.0653a10.10231,10.10231,0,0,0-.24091-4.03449,5.2482,5.2482,0,0,0-4.87311-3.1394q-.20114.0021-.4024.00378A5.23959,5.23959,0,0,0,6.92853,5.75293,10.08988,10.08988,0,0,0,6.68726,9.784q.01941.29872.036.59771a.8483.8483,0,0,1-.5838.17841,2.45322,2.45322,0,0,1-1.014-.26776.57538.57538,0,0,0-.2453-.04895.83387.83387,0,0,0-.81061.53265c-.08191.43061.5329.74256.90668.8902.079.03137.17822.0628.28308.096.42169.13385,1.05908.33606,1.25152.78985a1.07171,1.07171,0,0,1-.10223.89783l-.00537.01154a7.02828,7.02828,0,0,1-1.06915,1.66211,5.21488,5.21488,0,0,1-3.13483,1.86389.23978.23978,0,0,0-.20044.25006.38046.38046,0,0,0,.031.12964c.17578.41113,1.05822.75061,2.55182.981.13964.02161.19873.24927.28027.6222.03259.14929.06634.30426.1134.46423a.29261.29261,0,0,0,.31922.22876,2.48528,2.48528,0,0,0,.42492-.06091,5.52912,5.52912,0,0,1,1.12036-.12677,4.95367,4.95367,0,0,1,.8078.0683,3.87725,3.87725,0,0,1,1.535.78417,4.443,4.443,0,0,0,2.6897,1.06006c.03375,0,.06744-.00122.10009-.004.04114.00195.09522.004.15192.004a4.44795,4.44795,0,0,0,2.69122-1.06079,3.87269,3.87269,0,0,1,1.53351-.78332,4.97275,4.97275,0,0,1,.808-.0683,5.59252,5.59252,0,0,1,1.12037.11871,2.39142,2.39142,0,0,0,.425.05371h.02338a.279.279,0,0,0,.29547-.221c.04645-.15784.08045-.308.11389-.46131.08081-.371.1399-.59759.28009-.61926,1.494-.23078,2.37641-.56976,2.551-.97858a.38487.38487,0,0,0,.03174-.13086A.24.24,0,0,0,21.79755,16.98718Z' fill='%236563ff'/%3E%3C/svg%3E"/>
            </svg>
            {label}
        </a>
        </p>'''
    elif icon == 'tiktok':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={19} height={19} fill="currentColor" class="bi bi-Tiktok" viewBox="0 0 32 32">
                    <path d="m 22.912602,1.0567933 -5.289176,0.00154 V 22.894399 c 0,1.879824 -1.122255,3.556703 -2.858986,4.276081 -1.736733,0.719377 -3.714028,0.325441 -5.0432639,-1.003798 C 8.3919396,24.837447 7.998002,22.858082 8.7173793,21.121352 9.436757,19.38462 11.113635,18.264949 12.993459,18.264949 h 1.710535 v -5.289692 h -1.710535 c -4.0043223,0 -7.6309355,2.424009 -9.1633233,6.12352 -1.5323881,3.699511 -0.6818199,7.977799 2.149664,10.809282 2.8314833,2.831484 7.1102863,3.682051 10.8097973,2.149663 3.699513,-1.532388 6.123005,-5.159 6.123005,-9.163323 V 10.78633 c 1.440079,0.858005 3.141229,1.487871 5.23338,1.487871 h 2.643553 V 6.982964 h -2.643553 c -2.974623,0 -3.781104,-1.2098821 -4.487379,-2.7453293 C 22.953,2.7036478 22.912602,1.0567933 22.912602,1.0567933 Z" id="path5550" style="color:#6563ff;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:medium;line-height:normal;font-family:sans-serif;font-variant-ligatures:normal;font-variant-position:normal;font-variant-caps:normal;font-variant-numeric:normal;font-variant-alternates:normal;font-variant-east-asian:normal;font-feature-settings:normal;font-variation-settings:normal;text-indent:0;text-align:start;text-decoration:none;text-decoration-line:none;text-decoration-style:solid;text-decoration-color:#6563ff;letter-spacing:normal;word-spacing:normal;text-transform:none;writing-mode:lr-tb;direction:ltr;text-orientation:mixed;dominant-baseline:auto;baseline-shift:baseline;text-anchor:start;white-space:normal;shape-padding:0;shape-margin:0;inline-size:0;clip-rule:nonzero;display:inline;overflow:visible;visibility:visible;opacity:1;isolation:auto;mix-blend-mode:normal;color-interpolation:sRGB;color-interpolation-filters:linearRGB;solid-color:#6563ff;solid-opacity:1;vector-effect:none;fill:##6563ff;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:0.999725;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:0;stroke-dasharray:none;stroke-dashoffset:0;stroke-opacity:1;paint-order:fill markers stroke;color-rendering:auto;image-rendering:auto;shape-rendering:auto;text-rendering:auto;enable-background:accumulate;stop-color:#6563ff;stop-opacity:1"/>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == 'medium':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={19} height={19} fill="currentColor" class="bi bi-medium" viewBox="0 0 16 16">
                    <path d="M9.025 8c0 2.485-2.02 4.5-4.513 4.5A4.506 4.506 0 0 1 0 8c0-2.486 2.02-4.5 4.512-4.5A4.506 4.506 0 0 1 9.025 8zm4.95 0c0 2.34-1.01 4.236-2.256 4.236-1.246 0-2.256-1.897-2.256-4.236 0-2.34 1.01-4.236 2.256-4.236 1.246 0 2.256 1.897 2.256 4.236zM16 8c0 2.096-.355 3.795-.794 3.795-.438 0-.793-1.7-.793-3.795 0-2.096.355-3.795.794-3.795.438 0 .793 1.699.793 3.795z"/>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == 'newsletter':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={19} height={19} fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16">
                    <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z"/>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == 'cup':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-cup-fill" viewBox="0 0 16 16">
                    <path d="M1 2a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v1h.5A1.5 1.5 0 0 1 16 4.5v7a1.5 1.5 0 0 1-1.5 1.5h-.55a2.5 2.5 0 0 1-2.45 2h-8A2.5 2.5 0 0 1 1 12.5V2zm13 10h.5a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.5-.5H14v8z"/>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == '':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                {label}
            </a>
        </p>'''
    return st.markdown(button_code, unsafe_allow_html=True)
