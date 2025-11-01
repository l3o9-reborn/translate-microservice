import argostranslate.package
import argostranslate.translate

# Update package index
argostranslate.package.update_package_index()

# List available packages
available_packages = argostranslate.package.get_available_packages()
print(available_packages)

# Install en->fr
en_fr_package = next(p for p in available_packages if p.from_code == "en" and p.to_code == "fr")
argostranslate.package.install_from_path(en_fr_package.download())

# Install en->ar
en_ar_package = next(p for p in available_packages if p.from_code == "en" and p.to_code == "ar")
argostranslate.package.install_from_path(en_ar_package.download())

print("✅ Models installed successfully")
