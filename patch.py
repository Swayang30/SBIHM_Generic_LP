import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Desktop form replacement
start_marker = '<div class=\"elementor-element elementor-element-9afd730 elementor-widget elementor-widget-html\" data-id=\"9afd730\" data-element_type=\"widget\" data-e-type=\"widget\" data-widget_type=\"html.default\"><div class=\"elementor-widget-container\">\n'
# Note that in index.html, there's a newline between line 53 and 54!
# Wait, let's just use regex.

pattern_desktop = re.compile(r'(<div class=\"elementor-element elementor-element-9afd730 elementor-widget elementor-widget-html\" data-id=\"9afd730\" data-element_type=\"widget\" data-e-type=\"widget\" data-widget_type=\"html.default\"><div class=\"elementor-widget-container\">)(.*?)(</div></div></div></div></div></section></div></div></div></section>)', re.DOTALL)

desktop_form_html = '''
<div style="background: linear-gradient(180deg, #D4AF37 0%, rgba(30,58,138,0.9) 100%); padding: 35px 30px; border-radius: 20px; box-shadow: 0 15px 40px rgba(0,0,0,0.4); text-align: center; max-width: 400px; margin: 0 auto; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1);">
  <h2 style="color: #1e3a8a; font-size: 32px; font-weight: 800; margin-bottom: 25px; font-family: \\\'Outfit\\\', sans-serif; text-shadow: 1px 1px 0px rgba(255,255,255,0.5);">Enquire Now</h2>
  <form action="#" method="post" style="display: flex; flex-direction: column; gap: 15px;">
    <input type="text" placeholder="Enter Full Name*" required style="width: 100%; padding: 12px 15px; border-radius: 5px; border: none; font-size: 14px; outline: none; box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); font-family: \\\'Outfit\\\', sans-serif;" />
    <div style="display: flex; gap: 10px;">
      <div style="background: #fff; border-radius: 5px; padding: 10px 15px; display: flex; align-items: center; justify-content: center; gap: 5px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);">
        <img src="https://flagcdn.com/w20/in.png" alt="India Flag" style="width: 20px; height: 14px; border-radius: 2px;"> <span style="font-size: 14px; color: #555; font-weight: 500;">+91 ?</span>
      </div>
      <input type="tel" placeholder="Enter Your Mobile No.*" required style="flex: 1; padding: 12px 15px; border-radius: 5px; border: none; font-size: 14px; outline: none; box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); font-family: \\\'Outfit\\\', sans-serif;" />
    </div>
    <input type="email" placeholder="Enter Your Email Id" style="width: 100%; padding: 12px 15px; border-radius: 5px; border: none; font-size: 14px; outline: none; box-shadow: inset 0 1px 3px rgba(0,0,0,0.1); font-family: \\\'Outfit\\\', sans-serif;" />
    <div style="display: flex; align-items: flex-start; gap: 10px; text-align: left; margin-top: 5px;">
      <input type="checkbox" id="agree_desktop" required style="margin-top: 4px; cursor: pointer;" />
      <label for="agree_desktop" style="font-size: 12px; color: rgba(255,255,255,0.9); line-height: 1.4; font-weight: 400; font-family: \\\'Outfit\\\', sans-serif; cursor: pointer;">I agree to receive information regarding my submitted applications by signing up on SBIHM.*</label>
    </div>
    <button type="submit" style="background: #FFCA28; color: #1e3a8a; font-weight: 700; text-transform: uppercase; border: none; padding: 14px 30px; border-radius: 30px; margin-top: 10px; cursor: pointer; align-self: flex-end; box-shadow: 0 4px 15px rgba(255, 202, 40, 0.4); transition: all 0.3s ease; font-family: \\\'Outfit\\\', sans-serif; font-size: 16px; letter-spacing: 0.5px;" onmouseover="this.style.transform=\\\'translateY(-2px)\\\'; this.style.boxShadow=\\\'0 6px 20px rgba(255, 202, 40, 0.6)\\\';" onmouseout="this.style.transform=\\\'translateY(0)\\\'; this.style.boxShadow=\\\'0 4px 15px rgba(255, 202, 40, 0.4)\\\';">SUBMIT</button>
  </form>
</div>
'''

new_content = pattern_desktop.sub(rf'\\g<1>{desktop_form_html}\\g<3>', content)

# Now let's handle the mobile form. The mobile form is inside:
# <div class="elementor-element elementor-element-5a6e829 elementor-widget elementor-widget-shortcode" ...><div class="elementor-widget-container"><div class="elementor-shortcode"><div class="wpcf7 no-js" ...
# and ends with </form></div></div></div></div></div></div></div></section>
pattern_mobile = re.compile(r'(<div class=\"elementor-element elementor-element-5a6e829 elementor-widget elementor-widget-shortcode\".*?<div class=\"elementor-widget-container\">)(.*?)(</div></div></div></div></div></section>)', re.DOTALL)

# Let's verify we replaced something
if content == new_content:
    print("Desktop replace failed")
else:
    print("Desktop replace success")

final_content = pattern_mobile.sub(rf'\\g<1>{desktop_form_html}\\g<3>', new_content)

if new_content == final_content:
    print("Mobile replace failed")
else:
    print("Mobile replace success")
    
# Remove escapes we had to use for powershell payload
final_content = final_content.replace("\\'", "'")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_content)
