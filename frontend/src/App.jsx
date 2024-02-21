import { useState } from "react"

export default function App() {
  return (
    <>
      <div className="h-screen bg-dark-secondary">
        <div className="navbar flex flex-row h-[10%] justify-between w-screen bg-dark-primary fixed top-0 z-50">
          <div className="text-dark-accent font-mono font-extrabold pl-[5%] flex flex-row justify-center items-center logo w-[10%]">
            <p className="text-3xl hover:text-4xl hover:duration-150">GoVYA</p>  
          </div>
          <div className="flex flex-row items-center gap-16 px-20 text-light-primary text-lg font-semibold">
            <p className="hover:underline">Login</p>
            <p className="">|</p>
            <p className="hover:underline">Register</p>
          </div> 
        </div>
        <div className="h-screen video-background relative">
          <video autoPlay loop muted className="absolute inset-0 w-full h-full object-cover">
            <source src="./src/assets/video-2.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
          <div className="absolute inset-0 bg-dark-primary bg-opacity-[15%]"></div>
          <div className="w-1/2 text-light-primary flex flex-col justify-center items-center absolute inset-0 pr-[5%] ">
            <div className="group">
              <p className="text-5xl font-extrabold mb-4 group-hover:text-[3.2rem] group-hover:duration-150">Seamless <font className=" text-[#67d2ec]">Shipping,</font></p>
              <p className="text-5xl font-extrabold group-hover:text-[3.2rem] group-hover:duration-150">Instant <font className=" text-[#e7895d]">Connections</font></p>
            </div>
            <div>
            <hr class="border w-[22rem] border-light-primary mx-auto mt-[15%] mb-10"/>
            </div>
            <div className="group w-3/5 flex flex-col justify-center items-center font-bold text-lg font-mono text-light-primary pr-[1%]">
              <p className="group-hover:text-[1.150rem] group-hover:duration-150 ">Experience a new level of <span className="text-highlight-secondary">efficiency</span></p>
              <p className="group-hover:text-[1.150rem] group-hover:duration-150 ">in <span className="text-highlight-secondary">logistics</span>. Connect with top-tier</p>
              <p className="group-hover:text-[1.150rem] group-hover:duration-150 ">carriers <span className="text-highlight-secondary">instantly</span> , ensuring your</p>
              <p className="group-hover:text-[1.150rem] group-hover:duration-150 ">cargo reaches its <span className="text-highlight-secondary">destination</span> with</p>
              <p className="group-hover:text-[1.150rem] group-hover:duration-150 "> <span className="text-highlight-secondary">speed</span> and precision.</p>
            </div>

          </div>
          
        </div>
      </div>
      <div className="h-screen bg-light-primary"></div>
        <div className="contact flex flex-col w-screen h-[25%] bg-dark-secondary text-light-primary items-center ">
          <div className="w-[80%] flex flex-row text-justify m-10">
            <div className="w-1/3 flex flex-row justify-center">
              <div className="text-sm text-left">
                <p className="font-bold text-base">Contact Us :</p>
                <div className="">
                  <p><span className="italic pr-2">Address:  </span>GoVYA Packaging, Westind Country Club Rd, Industrial Area, Manipal, Karnataka - 576104</p>
                  <p><span className="italic pr-2">Email:  </span>govya@services.mail.com</p>
                  <p><span className="italic pr-2">Phone:  </span>+91 99876 56789</p>
                  <p><span className="italic pr-2">Telephone:  </span>+12 18432-232-423</p>
                </div>
              </div>
            </div>
            <div className="w-1/3 flex flex-row justify-center">
              <div className=""><div className="font-extrabold">
                <p>Disclaimer</p>
                </div>
                <div className="font-serif text-sm">
                  <p>Operational metrics listed are as of August 04, 2023. </p>
                  <p>GoVYA © ltd.</p>
                </div>
                <div className="font-serif text-sm m-5 flex flex-row justify-between">
                  <p className="hover:underline">Terms and Conditions</p>
                  <p>|</p>
                  <p className="hover:underline">Privacy Policy</p>
                </div>
              </div>
            </div>
            <div className="w-1/3 flex flex-row justify-center">
              <div className="text-justify">
                <p className="font-extrabold"> Information Security Policy</p>
                <p className="font-serif text-sm">GoVYA is committed to safeguarding the confidentiality, integrity and availability of all physical and electronic information assets of the organization.
We ensure that the regulatory, operational and contractual requirements are fulfilled.</p>
              </div>
            </div>
          </div>
        </div>
    </>
  )
}