"use client"

import { useState, useRef } from "react"
import { UserIcon, PhoneIcon, CameraIcon, ArrowUpIcon as ArrowUpTrayIcon } from "lucide-react"

const Home = () => {
  const [formData, setFormData] = useState({
    name: "",
    phone: "",
  })
  const [image, setImage] = useState(null)
  const [preview, setPreview] = useState(null)
  const [errors, setErrors] = useState({})
  const fileInputRef = useRef(null)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData({
      ...formData,
      [name]: value,
    })

    // Clear error when user types
    if (errors[name]) {
      setErrors({
        ...errors,
        [name]: null,
      })
    }
  }

  const handleImageChange = (e) => {
    const file = e.target.files[0]
    if (file) {
      setImage(file)
      const reader = new FileReader()
      reader.onloadend = () => {
        setPreview(reader.result)
      }
      reader.readAsDataURL(file)
    }
  }

  const triggerFileInput = () => {
    fileInputRef.current.click()
  }

  const validateForm = () => {
    const newErrors = {}

    if (!formData.name.trim()) {
      newErrors.name = "Name is required"
    }

    if (!formData.phone.trim()) {
      newErrors.phone = "Phone number is required"
    } else if (!/^\d{10}$/.test(formData.phone.replace(/\D/g, ""))) {
      newErrors.phone = "Please enter a valid 10-digit phone number"
    }

    if (!image) {
      newErrors.image = "Please upload an image"
    }

    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const handleSubmit = (e) => {
    e.preventDefault()

    if (validateForm()) {
      // Form submission logic would go here
      console.log("Form submitted:", { ...formData, image })
      alert("Form submitted successfully!")

      // Reset form
      setFormData({ name: "", phone: "" })
      setImage(null)
      setPreview(null)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-xl shadow-xl w-full max-w-md overflow-hidden">
        <div className="bg-gradient-to-r from-violet-500 to-purple-600 p-6 text-white">
          <h1 className="text-2xl font-bold">Info Form</h1>
          <p className="mt-2 opacity-90">Please fill in your details below</p>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-6">
          <div className="space-y-2">
            <label htmlFor="name" className="text-sm font-medium text-gray-700 flex items-center gap-2">
              <UserIcon size={16} />
              <span>Full Name</span>
            </label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className={`w-full px-4 py-3 rounded-lg border ${errors.name ? "border-red-500" : "border-gray-300"} focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition`}
              placeholder="Enter your full name"
            />
            {errors.name && <p className="text-red-500 text-xs mt-1">{errors.name}</p>}
          </div>

          <div className="space-y-2">
            <label htmlFor="phone" className="text-sm font-medium text-gray-700 flex items-center gap-2">
              <PhoneIcon size={16} />
              <span>Phone Number</span>
            </label>
            <input
              type="tel"
              id="phone"
              name="phone"
              value={formData.phone}
              onChange={handleChange}
              className={`w-full px-4 py-3 rounded-lg border ${errors.phone ? "border-red-500" : "border-gray-300"} focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition`}
              placeholder="Enter your phone number"
            />
            {errors.phone && <p className="text-red-500 text-xs mt-1">{errors.phone}</p>}
          </div>

          <div className="space-y-2">
            <label className="text-sm font-medium text-gray-700 flex items-center gap-2">
              <CameraIcon size={16} />
              <span>Upload Image</span>
            </label>

            <input type="file" ref={fileInputRef} onChange={handleImageChange} accept="image/*" className="hidden" />

            {preview ? (
              <div className="relative w-full h-48 rounded-lg overflow-hidden group">
                <img src={preview || "/placeholder.svg"} alt="Preview" className="w-full h-full object-cover" />
                <div
                  className="absolute inset-0 bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 flex items-center justify-center transition-opacity cursor-pointer"
                  onClick={triggerFileInput}
                >
                  <p className="text-white text-sm">Click to change</p>
                </div>
              </div>
            ) : (
              <div
                onClick={triggerFileInput}
                className={`w-full h-48 border-2 border-dashed ${errors.image ? "border-red-500" : "border-gray-300"} rounded-lg flex flex-col items-center justify-center cursor-pointer hover:border-purple-500 transition-colors`}
              >
                <ArrowUpTrayIcon size={32} className="text-gray-400 mb-2" />
                <p className="text-sm text-gray-500">Click to upload an image</p>
                <p className="text-xs text-gray-400 mt-1">JPG, PNG or GIF</p>
              </div>
            )}
            {errors.image && <p className="text-red-500 text-xs mt-1">{errors.image}</p>}
          </div>

          <button
            type="submit"
            className="w-full bg-gradient-to-r from-violet-500 to-purple-600 text-white py-3 rounded-lg font-medium hover:from-violet-600 hover:to-purple-700 transition-colors focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2"
          >
            Submit
          </button>
        </form>
      </div>
    </div>
  )
}


export default Home