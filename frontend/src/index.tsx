import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { Login, UserHome, Signup, Profile } from "pages";
import { SessionProvider } from "providers";

const root = ReactDOM.createRoot(
    document.getElementById("root") as HTMLElement
);

root.render(
    <React.StrictMode>
        <SessionProvider>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Login />} />
                    <Route path="/signup" element={<Signup />} />
                    <Route path="/user" element={<UserHome />} />
                    <Route path="/profile" element={<Profile />} />
                </Routes>
            </BrowserRouter>
        </SessionProvider>
    </React.StrictMode>
);

